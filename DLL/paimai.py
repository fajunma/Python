# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'
import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import sqlite3
u2018 = 'http://chepai.alltobid.com/contents/22/276.html'
u2017 = 'http://chepai.alltobid.com/contents/22/103.html'
def get_paimai_price(url):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'}
    target=requests.get(url,headers=headers)
    target.encoding='utf-8'
    history=BeautifulSoup(target.text,'lxml')

    cont=history.tbody.findAll('tr')
    for x in cont:
        tmp=[]
        for z in x.children:
            tmp.append(z.span.text)
        info.append(tmp)
    # for x in info:
    #     print(x)
        #print('C--',z.span.text)
    #print(type(x))
    #print(x.td.prettify())
    # td=x.findAll('td')
    # for y in td:
    #     print(y)
    # if 'width' in x:
    #     pass
    # else:



#print(history.tbody.tr.prettify())

#print(tr[0])
# print(cont)
#nums=re.findall('<span style=?font-size:16px;\?>([0-9]+)</span>',history)
# nums=re.findall('<td align="center"><span style="font-size:16px;">([0-9]+)</span>',str(history))
# for x in nums:
#     print(x)
# price=[int(x) for x in nums]
# print('平均价格是--',sum(price)//len(price),'\nMax--',max(price),'\nLowest--',min(price))

if __name__=="__main__":
    u2018 = 'http://chepai.alltobid.com/contents/22/281.html'
    u2017 = 'http://chepai.alltobid.com/contents/22/103.html'
    info = []

    conn = sqlite3.connect('price.db')
    cur = conn.cursor()
    try:
        cur.execute('''CREATE TABLE PRICE2018
                       (拍卖时间 CHAR[50]    ,
                       投放数量 CHAR[50]   ,
                       最低成交价格 CHAR[50]     ,
                       平均成交价格 CHAR[50]   ,
                       投标人数 CHAR[50]  ,
                       最低成交价格截止时间  CHAR[50]   );''')
    except:
        pass

    dt = cur.execute('SELECT * FROM PRICE2018 ')
    for x in dt:
        print('database--', x[0])

    # dt=cur.execute('SELECT * FROM PRICE2018 GROUP BY 拍卖时间 HAVING COUNT(*)>1')
    # for x in dt:
    #     print('REP--',x)

    # cur.execute("DELETE FROM PRICE2018 WHERE 拍卖时间='2018年5月'")
    cur.execute('DELETE FROM PRICE2018 WHERE ROWID NOT IN (SELECT MIN(ROWID) FROM PRICE2018 GROUP BY 拍卖时间)')

    dt = cur.execute('SELECT * FROM PRICE2018 ')
    for x in dt:
        print('database--', x)


    # NAME=cur.execute('SELECT * FROM PRICE2018 WHERE type=’拍卖时间’ ')
    # print(NAME)
    #get_paimai_price(u2017)
    get_paimai_price(u2018)
    reslt=[]
    seconds=[]
    avg=[]
    date=[]
    lowest=[]
    for x in info:
        if x not in reslt:
            reslt.append(x)
    for x in reslt[1:]:
        print(x)
        # sqlone = "INSERT INTO PRICE2018 VALUES(%s)" % (','.join(x))
        # cur.execute(sqlone)
        try:
            sqlone = "INSERT INTO PRICE2018(拍卖时间,投放数量,最低成交价格,平均成交价格,投标人数,最低成交价格截止时间) VALUES{0}".format(tuple(x))
            cur.execute(sqlone)
            seconds.append(int(x[4][6:9]))
            lowest.append(float(x[2]))
            avg.append(float(x[3]))
            date.append (datetime.strptime(x[0], '%Y年%m月'))
        except:
            pass

    print(reslt)

    conn.commit()
    conn.close()



    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(date,seconds,'*-r')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%y-%m'))
    plt.gcf().autofmt_xdate()  # 自动旋转日期标记
    plt.title(r'2018 LAST SECONDS')
    plt.xlabel(r'$\alpha =\frac{1}{2}\ln(\frac{1-\varepsilon}{\varepsilon })$')
    plt.ylabel(r'y =last second')
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(date, lowest, '*-g')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%y-%m'))
    plt.gcf().autofmt_xdate()  # 自动旋转日期标记
    plt.title(r'2018 shanghai BID LOWEST PRICE')
    plt.xlabel(r'$\alpha =\frac{1}{2}\ln(\frac{1-\varepsilon}{\varepsilon })$')
    plt.ylabel(r'y =last second')
    plt.grid()
    plt.show()

    # print(sum(avg)/len(avg))
