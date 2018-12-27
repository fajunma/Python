# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'

import pyautogui as pag
from PIL import ImageGrab
import time
import pygame

# pygame.init()
# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.KEYDOWN:
#             print('向右移动')

while True:
    x,y=pag.position()
    print('--',str(x),'--',str(y))
    time.sleep(1)

bbox = (1000, 500, 1920,1080)
im = ImageGrab.grab(bbox)
im.save('snap.png')


