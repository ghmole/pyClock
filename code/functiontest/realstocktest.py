from libs.urllib import urequest
from machine import Pin
import network,time

#定义常用颜色
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

class StockData():
    def __init__(self):
        self.stock_name = ''
        self.stock_code = ''
        self.last_price = ''
        self.pre_close = ''
        self.open_price = ''
        self.low_price = ''
        self.high_price = ''
        self.avg_price = ''



class QuoteSourceQtimg():
    def __init__(self):
        self.d=StockData()
        
    def query_stock(self,code):

        d = StockData()
        try:
            my_url='http://qt.gtimg.cn/r=0.9392363841179758&q='+code
            print(my_url)
            my_req = urequest.urlopen(my_url)

            # 坏消息micropython 不支持gbk编码
            res = my_req.read(900)#.decode('gbk') #抓取约前4W个字符，节省内存。
           
            res=str(res)
            print(res)
           
            
            for line in res.split(';'):
                #print line
                if len(line) < 50 :
                    continue
                info = line[12: 100]
                #print info
                vargs = info.split('~')
                #print vargs
                d.stock_name = vargs[1]
                d.stock_code = vargs[2]
                d.last_price = vargs[3]
                d.pre_close = vargs[4]
                d.open_price = vargs[5]
                d.low_price = ''
                d.high_price = ''
                d.avg_price = ''
            self.d=d
        except Exception as ex:
            print("Can not get stock!",code)
            print(type(ex),dir(ex))
            print(ex.errno, len(ex.args), ex.value)
            print(repr(ex))
             
            gc.collect() #内存回收
            
        self.print_stock(d)

    def print_stock(self,d):
        print('stock_name: %s\n' % d.stock_name)
        print('stock_code: %s\n' % d.stock_code)
        print('last_price: %s\n' % d.last_price)
        print('pre_close: %s\n' % d.pre_close)
        print('open_price: %s\n' % d.open_price)
        print('low_price: %s\n' % d.low_price)
        print('high_price: %s\n' % d.high_price)
        print('avg_price: %s\n' % d.avg_price)
   

#WIFI连接函数
def WIFI_Connect():

    WIFI_LED=Pin(2, Pin.OUT) #初始化WIFI指示灯

    WIFI_LED.value(0)
    wlan = network.WLAN(network.STA_IF) #STA模式
    wlan.active(False)
    time.sleep(1)
    wlan.active(True)                   #激活接口
    start_time=time.time()              #记录时间做超时判断

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('H68K', 'xzx0606xzx') #输入WIFI账号密码

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
    
       
#执行WIFI连接函数
WIFI_Connect()
qt=QuoteSourceQtimg()
qt.query_stock('sh600006')

