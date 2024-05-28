import machine
import time

# 设置引脚4、5、6、7为输入
pin4 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
pin5 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
pin6 = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
pin7 = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_UP)

# 保存上一次状态的字典
last_states = {4: pin4.value(), 5: pin5.value(), 6: pin6.value(), 7: pin7.value()}

while True:
    # 检查引脚状态是否有变化
    if pin4.value() != last_states[4]:
        print("Pin 4状态变化:", "高电平" if pin4.value() else "低电平")
        last_states[4] = pin4.value()
    if pin5.value() != last_states[5]:
        print("Pin 5状态变化:", "高电平" if pin5.value() else "低电平")
        last_states[5] = pin5.value()
    if pin6.value() != last_states[6]:
        print("Pin 6状态变化:", "高电平" if pin6.value() else "低电平")
        last_states[6] = pin6.value()
    if pin7.value() != last_states[7]:
        print("Pin 7状态变化:", "高电平" if pin7.value() else "低电平")
        last_states[7] = pin7.value()
    
    time.sleep(0.1)  # 避免过于频繁地检查状态变化




import machine
import time

# 定义接口列表
pin_list = [1,2,3,4,5,6,7,8,9]  # 这里只是示例，可以根据需要修改

# 初始化所有接口为输入模式
for pin_num in pin_list:
    pin = machine.Pin(pin_num, machine.Pin.IN)

# 创建一个字典，用于存储上一次读取的接口电平
last_values = {pin_num: None for pin_num in pin_list}

# 无限循环监视接口电平变化
while True:
    for pin_num in pin_list:
        pin = machine.Pin(pin_num)
        current_value = pin.value()

        # 如果当前电平与上一次不同，则打印输出接口编号
        if current_value != last_values[pin_num]:
            print("接口 {} 的电平发生变化，当前电平为 {}".format(pin_num, current_value))
            last_values[pin_num] = current_value

    # 延迟一段时间再次检查
    time.sleep(0.2)

