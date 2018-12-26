# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b      # 使用 yield
        a, b = b, a + b
        n = n + 1
def enu(n):
    for x in range(n):
        yield  x
def ecp(*kx,**ky):
    print('kiahis')
    for y in kx:
        print(y)
    for key,val in ky.items():
        print(key,'__',val)

if __name__=="__main__":
    for x in enu(7):
        print(x,'---')
    print(enu(6))

    ecp(3.2,[7,4,9],op=3,kl=1.09)