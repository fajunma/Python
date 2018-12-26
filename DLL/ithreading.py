# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'

#coding=utf-8
import threading
from time import ctime,sleep


def music(func):
    for i in range(20):
        print( "I was listening to %s. %s" %(func,ctime()))
        sleep(100)

def move(func):
    for i in range(20):
        print( "I was at the %s! %s" %(func,ctime()))
        sleep(200)


if __name__ == '__main__':
    threads = [threading.Thread(target=music, args=(u'爱情买卖',)),threading.Thread(target=move, args=(u'阿凡达',))]

    for t in threads:
        t.setDaemon(True)
        t.start()

    print ("all over %s" %ctime())