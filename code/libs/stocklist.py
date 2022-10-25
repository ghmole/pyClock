import os
stocklist=['sh600006'];
# 读股票代码
def read_stock_list():
    global stocklist
    # 股票代码文件是否存在
    if 'stocklist.txt' in os.listdir('.'): 
        # 读文件，注意文件编码
        f = open('./stocklist.txt', 'r',encoding='gbk')
        
        # 读一行
        stockcode = f.readline()
        while (stockcode):
            # 测试
            print(stockcode.replace('\n',''),stockcode.encode('gbk'))
            # 删除换行
            stockcode=stockcode.replace('\n','')
            # 如果不在列表里面，则添加
            if not stockcode in stocklist:
                stocklist.append(stockcode)
            # 读下一行   
            stockcode = f.readline()

        f.close()
    return stocklist
        
# 保存股票代码        
def write_stock_list():
    global stocklist
    # 打开文件，主要编码
    f = open('./stocklist.txt', 'wt',encoding='gbk')

    # 逐个写入股票代码
    for i in range(len(stocklist)):
        stockcode=stocklist[i]

        f.write(stockcode)
        # print(i, len(stocklist))
        # 写入换行
        if i!=len(stocklist)-1:
            f.write('\n')

    f.close()