import network
import _thread
import socket
import time
import machine

# 配置WLAN接口
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Hkdaqian-SMART', 'daqianzhineng')

# 配置静态IP
静态IP = '192.168.1.120'
子网掩码 = '255.255.255.0'
网关 = '192.168.1.1'
DNS服务器 = '223.5.5.5'
wlan.ifconfig((静态IP, 子网掩码, 网关, DNS服务器))

# 其他配置
监听端口 = 10000
目标IP地址 = '192.168.1.30'  # 根据需要修改
目标端口 = 10000  # 根据需要修改
特定指令 = b'AL'  # 假设接收到的特定指令是'Receive'
发送指令 = b'DDAL'  # 向指定IP发送的指令

gpio_pin = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)

def 监听线程():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((静态IP, 监听端口))
    print("UDP监听器正在运行...")
    while True:
        数据, 地址 = udp_socket.recvfrom(1024)
        print(f"从{地址}接受到数据：{数据}")
        if 数据 == 特定指令:
            _thread.start_new_thread(发送线程, ())
        time.sleep(0.2)
    udp_socket.close()

def gpio监听线程():
    print("GPIO监听器正在运行...")
    上次状态 = 1  # 假设初始状态为高电平
    防抖时间 = 0.05  # 50毫秒的防抖时间
    while True:
        当前状态 = gpio_pin.value()
        if 当前状态 == 0 and 上次状态 == 1:
            # 如果状态从高变低，防抖并发送UDP指令
            time.sleep(防抖时间)
            # 再次检查确认状态确实变为低
            if gpio_pin.value() == 0:
                发送线程()
        上次状态 = 当前状态
        time.sleep(0.2)  # 每次检测间隔100毫秒


def 发送线程():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(发送指令, (目标IP地址, 目标端口))
    print(f"向{目标IP地址}:{目标端口}发送了指令")
    udp_socket.close()

# 确保WLAN连接成功
while not wlan.isconnected():
    pass

print('网络配置：', wlan.ifconfig())

# 启动监听线程
_thread.start_new_thread(监听线程, ())
_thread.start_new_thread(gpio监听线程())

while True:
    pass
