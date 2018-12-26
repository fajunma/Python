from tkinter import *
import time
import winsound
from playsound import playsound
class App(object):
    '''这是一个拍卖牌照的小闹钟'''
    def __init__(self, master):
        # 使用Frame增加一层容器
        fm1 = Frame(master)
        fm1.pack(side=TOP, fill=BOTH)  # , expand=YES)
        # Button是一种按钮组件，与Label类似，只是多出了响应点击的功能
        Label(fm1, text="闹钟响的时间：").pack(side=LEFT)
        e_time = StringVar()
        e_time.set('11:00:00')
        self.en = Entry(fm1, textvariable=e_time)
        self.en.pack(side=LEFT)  # ,expand=1,fill=X)


        fm2 = Frame(master)
        fm2.pack(side=TOP, fill=BOTH)  # , expand=YES)
        self.lbl = Label(fm2,text=time.strftime('%H:%M:%S', time.localtime(time.time())))
        self.lbl.config(fg='red',font=("rome", 50))
        self.lbl.pack()
        self.trick_it()

        fm3 = Frame(master)
        fm3.pack(side=BOTTOM, fill=BOTH)  # , expand=YES)

        self.BtnOpen = Button(fm3, text='验证格式'  ,command=self.verify_time_str)
        self.BtnOpen.pack(side=LEFT)
        # self.lb_in = Label(fm3, text='输入格式正确✔')
        # self.lb_in.pack(side=LEFT)

    def trick_it(self):
       #ms='%.01f'%((int(time.time()*10 00)-int(time.time())*1000)/1000)
        currentTime = time.strftime('%H:%M:%S', time.localtime(time.time()))
        self.lbl.config(text=currentTime)#+ms[1:])

        if currentTime!=self.en.get():
            self.lbl.after(10, self.trick_it)
        else:
            # music = 'Good Time.wav'
            playsound('apple.mp3')
                #winsound.PlaySound('apple.mp3', winsound.SND_ALIAS)
    def verify_time_str(self):
        try:
            time.strptime(self.en.get(), '%H:%M:%S')
            self.tm_str = True
        except:
            self.tm_str= False
        self.BtnOpen.config(text=str(self.tm_str)*15+'\n@'+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+'\nVERYFY AGAIN?')


if __name__ == "__main__":
    root = Tk()
    root.title("拍卖牌照的小闹钟")
    App(root)
    root.mainloop()
