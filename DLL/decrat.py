# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'
import time

def w1(func):
    print("---正在装饰1----",time.time())
    def inner(*args, **kwargs):
        print("---1111111111----")
        func(*args, **kwargs)
        print('America-completed-',time.time())
    return inner

@w1
def f1(a):
    b=input('you keybaod content?')
    print("---%d---" , a+b)

if __name__ == '__main__':
    xyz='Iraq'
    f1(xyz)
