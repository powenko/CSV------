__author__ = "Powen Ko, www.powenko.com"
"""
你好， 我是柯博文老師
測試 2,  20220414 01:35 pm
"""

import matplotlib.pyplot as plt
import csv



list1=[]
listClose=[]   # 收盤價
listDate=[]    # 日期
listOpen=[]    # 開盤價
listVolume=[]  # Volume 成交量
listSM5=[]     # SM5
listSM10=[]     # SM10
listDiff=[]    # 漲跌


#def SMA(x=0,sm=5,listClose):
def SMA(listClose,sm=5,x=0):
    total = 0
    if x >= sm:
        for day in range(x, x - sm, -1):
            print(total, listClose[day], day)
            total = total + float(listClose[day])
            print(total)
        total = total / (sm)
        print(total)
    else:
        total = float(listClose[x])  # 前五天
    # listSM5.append(total)
    return total

with open('2330.TW.csv', 'r',encoding="utf-8") as fin:
        read = csv.reader(fin, delimiter=',')
        header = next(read)   # 讀擋頭
        print(header)
        x=0
        for row in read:
            print(row[1])
            #if  (int(row[7])==2021 and   int(row[8])==1):  # 2008 01
            list1.append(int(x))
            listClose.append(float(row[4]))      # close
            listOpen.append(float(row[1]))      # open
            listVolume.append(float(row[6]))      # 開盤價
            listDate.append(row[0])            # 日期

            ### sm5 的計算 start
            t1=SMA(listClose, 5, x)
            listSM5.append(t1)
            ### sm5 的計算 end
            ### sm10 的計算 start
            t1=SMA(listClose, 10, x)
            listSM10.append(t1)
            ### sm10 的計算 end


            x=x+1
        plt.subplot(3, 1, (1, 2))
        plt.plot(list1,listClose, 'r-',label="close")
        plt.plot(list1,listOpen, 'b-',label="open")
        plt.plot(list1,listSM5, 'g-',label="SM5")
        plt.plot(list1,listSM10, 'k-',label="SM10")
        plt.title('open-close')
        plt.legend()

        plt.subplot(3, 1, (3))
        plt.title('Volume')
        plt.plot(list1, listVolume, 'r-', label="Volume")
        plt.legend()
        plt.show()
