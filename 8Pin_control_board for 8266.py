from socket import *
import network
import time
from machine import Pin

kg1=Pin(4,Pin.OUT)
kg2=Pin(13,Pin.OUT)
kg3=Pin(15,Pin.OUT)
kg4=Pin(16,Pin.OUT)
kg5=Pin(12,Pin.OUT)
kg6=Pin(14,Pin.OUT)
kg7=Pin(5,Pin.OUT)
kg8=Pin(0,Pin.OUT)
ledp=Pin(2,Pin.OUT)
kg1.value(0)
kg2.value(0)
kg3.value(0)
kg4.value(0)
kg5.value(0)
kg6.value(0)
kg7.value(0)
kg8.value(0)
ledp.value(1)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.scan()
wlan.isconnected()
wlan.connect('ctrl', 'yk123456')
wlan.config('mac')
wlan.ifconfig(('192.168.1.30','255.255.255.0','192.168.1.1','192.168.1.1'))

udp = socket(AF_INET, SOCK_DGRAM)
udp.bind(('192.168.1.30', 10000))
while True:
    rec_msg, addr = udp.recvfrom(1024)
#    client_ip, client_port = addr
#    print('client_ip:', client_ip, 'client_port:', client_port)
#    print('msg from client:', rec_msg.decode('utf8'))
#    ack_msg = 'Hello, udp client.'
#    udp.sendto(ack_msg.encode('utf8'), addr)
    if rec_msg.decode('utf8') == 'ON01':
        kg1.value(1)
    elif rec_msg.decode('utf8') == 'FF01':
        kg1.value(0)
    elif rec_msg.decode('utf8') == 'ON02':
        kg2.value(1)
    elif rec_msg.decode('utf8') == 'FF02':
        kg2.value(0)
    elif rec_msg.decode('utf8') == 'ON03':
        kg3.value(1)
    elif rec_msg.decode('utf8') == 'FF03':
        kg3.value(0)
    elif rec_msg.decode('utf8') == 'ON04':
        kg4.value(1)
    elif rec_msg.decode('utf8') == 'FF04':
        kg4.value(0)
    elif rec_msg.decode('utf8') == 'ON05':
        kg5.value(1)
    elif rec_msg.decode('utf8') == 'FF05':
        kg5.value(0)
    elif rec_msg.decode('utf8') == 'ON06':
        kg6.value(1)
    elif rec_msg.decode('utf8') == 'FF06':
        kg6.value(0)
    elif rec_msg.decode('utf8') == 'ON07':
        kg7.value(1)
    elif rec_msg.decode('utf8') == 'FF07':
        kg7.value(0)
    elif rec_msg.decode('utf8') == 'ON08':
        kg8.value(1)
    elif rec_msg.decode('utf8') == 'FF08':
        kg8.value(0)
    elif rec_msg.decode('utf8') == 'ONAL':
        kg1.value(1)
        time.sleep_ms(500)
        kg2.value(1)
        time.sleep_ms(500)
        kg3.value(1)
        time.sleep_ms(500)
        kg4.value(1)
        time.sleep_ms(500)
        kg5.value(1)
        time.sleep_ms(500)
        kg6.value(1)
        time.sleep_ms(500)
        kg7.value(1)
        time.sleep_ms(500)
        kg8.value(1)
    elif rec_msg.decode('utf8') == 'FFAL':
        kg1.value(0)
        time.sleep_ms(500)
        kg2.value(0)
        time.sleep_ms(500)
        kg3.value(0)
        time.sleep_ms(500)
        kg4.value(0)
        time.sleep_ms(500)
        kg5.value(0)
        time.sleep_ms(500)
        kg6.value(0)
        time.sleep_ms(500)
        kg7.value(0)
        time.sleep_ms(500)
        kg8.value(0)
    elif rec_msg.decode('utf8') == 'DD01':
        kg1.value(1)
        time.sleep_ms(100)
        kg1.value(0)
    elif rec_msg.decode('utf8') == 'DD02':
        kg2.value(1)
        time.sleep_ms(100)
        kg2.value(0)
    elif rec_msg.decode('utf8') == 'DD03':
        kg3.value(1)
        time.sleep_ms(100)
        kg3.value(0)
    elif rec_msg.decode('utf8') == 'DD04':
        kg4.value(1)
        time.sleep_ms(100)
        kg4.value(0)
    elif rec_msg.decode('utf8') == 'DD05':
        kg5.value(1)
        time.sleep_ms(100)
        kg5.value(0)
    elif rec_msg.decode('utf8') == 'DD06':
        kg6.value(1)
        time.sleep_ms(100)
        kg6.value(0)
    elif rec_msg.decode('utf8') == 'DD07':
        kg7.value(1)
        time.sleep_ms(100)
        kg7.value(0)
    elif rec_msg.decode('utf8') == 'DD08':
        kg8.value(1)
        time.sleep_ms(100)
        kg8.value(0)        
    elif rec_msg.decode('utf8') == 'DDAL':
        kg1.value(1)
        time.sleep_ms(100)
        kg1.value(0)
        time.sleep_ms(500)
        kg2.value(1)
        time.sleep_ms(100)
        kg2.value(0)
        time.sleep_ms(500)
        kg3.value(1)
        time.sleep_ms(100)
        kg3.value(0)
        time.sleep_ms(500)
        kg4.value(1)
        time.sleep_ms(100)
        kg4.value(0)
        time.sleep_ms(500)
        kg5.value(1)
        time.sleep_ms(100)
        kg5.value(0)
        time.sleep_ms(500)
        kg6.value(1)
        time.sleep_ms(100)
        kg6.value(0)
        time.sleep_ms(500)
        kg7.value(1)
        time.sleep_ms(100)
        kg7.value(0)
        time.sleep_ms(500)
        kg8.value(1)
        time.sleep_ms(100)
        kg8.value(0) 