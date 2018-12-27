# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'

from pynput import keyboard
from pynput import mouse

# def on_press(key):
#     try:
#         print('press--{0}--'.format(key.char))
#     except:
#         pass
#
# def on_release(key):
#     try:
#         print('relse--{0}--'.format(key.char))
#         if key==keyboard.Key.esc:
#             return False
#     except:
#         pass
#
# with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
#     listener.join()



def on_move(x, y ):
    print('Pointer moved to {0}'.format(
        (x,y)))

def on_click(x, y , button, pressed):
    print('{0} at {1}--{2}'.format('Pressed' if pressed else 'Released', (x, y),button))
    if not pressed:
        return False

def on_scroll(x, y ,dx, dy):
    print('scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

while True:
    with mouse.Listener( no_move = on_move,on_click = on_click,on_scroll = on_scroll) as listener:
        listener.join()