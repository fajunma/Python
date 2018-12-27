# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'

import pytesseract
from PIL import Image
from PIL import ImageGrab
from pynput import mouse
import re
import time


bbox=[]
def on_click(x, y , button, pressed):
    print('{0} at {1} by mouse {2}'.format('Pressed' if pressed else 'Released', (x, y),button))
    if pressed:
        bbox.append([x,y])
    if len(bbox)==2:
        return False

with mouse.Listener( on_click = on_click) as listener:
    listener.join()

bbox=[y for x in bbox for y in x]

while True:
    print(bbox)
    im = ImageGrab.grab(bbox)
    #image=im
    im.save('snap.png')
    image = Image.open('snap.png')
    code = pytesseract.image_to_string(image,lang='chi_sim')
    print(code)
    indx=[ int(x) for x in re.findall('[0-9]{5,5}',code)]
    try:
        indx=[x for x in filter(lambda x: x>80000 and x<90000,indx)]
        print('当前时间是：',time.strftime('%H:%M:%S', time.localtime(time.time())),'当前的价格是RMB:',sum(indx)/len(indx))
    except:
        print('牌照拍买解释')
        break
    #time.sleep(1)
