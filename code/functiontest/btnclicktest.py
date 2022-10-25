from machine import Pin
import time


LED=Pin(2,Pin.OUT) #构建 LED 对象,开始熄灭
KEY=Pin(9,Pin.IN,Pin.PULL_UP) #构建 KEY 对象
state=0 #LED 引脚状态
nclick=0  # 点击次数
lastclicktime=0


#LED 状态翻转函数
def funcFalling(KEY):
    global state
    global nclick
    global lastclicktime
    time.sleep_ms(10) #消除抖动
#     print('F',time.ticks_ms(),lastclicktime)
#     print('F',time.ticks_ms()-lastclicktime)
    if KEY.value()==0: #确认按键被按下
        state = not state
        LED.value(state)
        print('*'*30)
        print(time.ticks_ms(),lastclicktime)
        print(time.ticks_ms()-lastclicktime)
        
        
        
        if time.ticks_ms()-lastclicktime<400:
            nclick+=1
        else:
            nclick=1
        lastclicktime=time.ticks_ms()
        print('nclick %d' % (nclick))
          
         
        
# def funcRaising(KEY):
#     global state
#     global nclick
#     global lastclicktime
#     time.sleep_ms(50) #消除抖动
#     
#    
#     if KEY.value()==1: #确认按键被释放
#         print('*'*30)
#         print('R',time.ticks_ms(),lastclicktime)
#         print('R',time.ticks_ms()-lastclicktime)
#          
#         if time.ticks_ms()-lastclicktime<=500:
#             nclick+=1
#         else:
#           nclick=0
#         print('nclick %d' % (nclick))
#         lastclicktime=time.ticks_ms()
#
def CheckClickNumber():
    global nclick
    
    
    if nclick>0:
        print('Key presss %d times' % nclick)
        nclick=0

KEY.irq(funcFalling,Pin.IRQ_FALLING) #定义中断，下降沿触发
# KEY.irq(funcRaising,Pin.IRQ_RISING) #定义中断，下降沿触发

while True:
    if time.ticks_ms()-lastclicktime>1000:
        CheckClickNumber()
        
    time.sleep_ms(100)