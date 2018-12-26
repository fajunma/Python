# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'

from PIL import Image
import numpy as np
import dill
import os
import sys
import time

img=Image.open('tp1.jpg')#彩色
#img=img.convert('L')#灰色
# img.save('gray.jpg')#保存
#r,g,b=img.getpixel((1,2))#获得某一像素点的值；
width,heigth=img.size

data=img.getdata(0) #获取红色的选项
data=np.matrix(data)

print(np.max(data),'MIN--',np.min(data),'本次图片的反射率平均值：',data.sum()/data.shape[1])
data=data.reshape(heigth,width)
im=Image.fromarray(data)
im.show()



#存储本次调试的中间值
dill.dump_session(os.getcwd() + '\\'+os.path.basename(sys.argv[0]).split(".")[0]+time.strftime('%Y-%m-%d',time.localtime(time.time()))+'.pkl')#存储所有中间变量
# dill.load_session(os.getcwd() + '\\'+os.path.basename(sys.argv[0]).split(".")[0]+time.strftime('%Y-%m-%d',time.localtime(time.time()))+'.pkl')
# im.show()