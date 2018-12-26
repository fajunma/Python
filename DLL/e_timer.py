# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'


import winsound # 导入此模块实现声音播放功能
import time # 导入此模块，获取当前时间 # 提示用户设置时间和分钟
my_hour = input("请输入时：")
my_minute = input("请输入分：")
my_second = input("请输入秒：")
flag = 1
while flag:
    t = time.localtime() # 当前时间的纪元值

    now = time.strftime("%H:%M:%S", t).split(':') # 将纪元值转化为包含时、分的字符串
    #now = now.split(':') #以空格切割，将时、分放入名为now的列表中
    hour = now[0]
    minute = now[1]
    second=now[2]
    if hour == my_hour and minute == my_minute and second==my_second:
        print('good!!')
        while True:
            #music = 'Good Time.wav'
            winsound.PlaySound('ALARM', winsound.SND_ALIAS)
        flag = 0
