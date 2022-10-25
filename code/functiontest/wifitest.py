'''
实验名称：连接无线路由器
版本：v1.0
日期：2022.5
作者：01Studio
说明：编程实现连接路由器，将IP地址等相关信息通过LCD显示（只支持2.4G网络）。
'''
import network,time
from machine import Pin
from tftlcd import LCD15

#定义常用颜色
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

########################
# 构建1.5寸LCD对象并初始化
########################
d = LCD15(portrait=1) #默认方向竖屏

#填充白色
d.fill(WHITE)

#WIFI连接函数
def WIFI_Connect():

    WIFI_LED=Pin(2, Pin.OUT) #初始化WIFI指示灯

    wlan = network.WLAN(network.STA_IF) #STA模式
    wlan.active(True)                   #激活接口
    start_time=time.time()              #记录时间做超时判断

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('TP-LINK_0', 'TL-112233') #输入WIFI账号密码

        while not wlan.isconnected():

            #LED闪烁提示
            WIFI_LED.value(1)
            time.sleep_ms(300)
            WIFI_LED.value(0)
            time.sleep_ms(300)

            #超时判断,15秒没连接成功判定为超时
            if time.time()-start_time > 15 :
                print('WIFI Connected Timeout!')
                wlan.active(False) #反使能WiFi
                break

    if wlan.isconnected():
        #LED点亮
        WIFI_LED.value(1)

        #串口打印信息
        print('network information:', wlan.ifconfig())
        
        #显示IP信息
        d.printStr('IP/Subnet/GW:',10,10,color=BLUE,size=2)
        d.printStr(wlan.ifconfig()[0],10,50,color=BLACK,size=2)
        d.printStr(wlan.ifconfig()[1],10,80,color=BLACK,size=2)
        d.printStr(wlan.ifconfig()[2],10,110,color=BLACK,size=2)

#执行WIFI连接函数
WIFI_Connect()
