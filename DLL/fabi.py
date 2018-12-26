# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'

def han_list(n,frm,to,temp):
    if n<2:
        to.append(frm.pop())
    else:
        fabi(n-1,frm,temp,to)
        fabi(1,frm,to,temp)
        fabi(n-1,temp,to,frm)


def fabi(n,frm,to,temp):

    if n<2:
        print(frm,'-->',to)
        s1.append([frm,'-->',to])

    else:
        fabi(n-1,frm,temp,to)
        #print('a----', n, '--from', frm, 'to', to, 'temp', temp)
        fabi(1,frm,to,temp)
        #to.append(frm.pop())
        #print('a----', n, '--from', frm, 'to', to, 'temp', temp)
        fabi(n-1,temp,to,frm)
        #print('a----', n, '--from', frm, 'to', to, 'temp', temp)
def hanoi(n, a, b, c):
    if n == 1:
        s2.append([a, '-->', c])
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        s2.append([a, '-->', c])
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)
# 调用


def fact(n):
    if n<2:
        return 1
    else:
        y=n*fact(n-1)
        print('n=',n,'---',y)
        return y
if __name__ == "__main__":
    nx=3
    a=[x for x in range(nx)]
    b,c=[],[]
    s1,s2=[],[]
    fabi(nx,'A','C','B')
    print('daan')
    hanoi(nx, 'A', 'B', 'C')
    if s1==s2:
        print(True)
    else:
        print('YIMA')
        print(s1)
        print(s2)
