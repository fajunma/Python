# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'

def w1(func):
    print("---正在装饰1----")
    def inner(*args, **kwargs):
        print("---1111111111----")
        func(*args, **kwargs)
    return inner

@w1
def f1(a):
    print("---%d---" , a)

xyz=input('frd:')
f1(xyz)

