# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'
import time
import random
import sys
sys.setrecursionlimit(1000000)  # 例如这里设置为一百万
def x_timer(f):
    def timing(*args):
        t1=time.clock()
        rt=f(*args)
        print('整个运行过程中wast_time:',time.clock()-t1,'秒')
        return  rt
    return timing

@x_timer
def x_sort(lst):
    lst.sort()
    return  lst


@x_timer
def y_sort(lst):
    return  sorted(lst)

@x_timer
def z_sort(lst):
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if lst[i]>lst[j]:
                t=lst[i]
                lst[i]=lst[j]
                lst[j]=t
    return lst

def quik_sort(lst):
    if len(lst)<2:
        return lst
    else:
        small=[]
        big=[]
        equal=[]
        base=lst[0]
        for x in lst:
            if x>base:
                big.append(x)
            elif x<base:
                small.append(x)
            else:
                equal.append(x)
        return quik_sort(small)+equal+quik_sort(big)

def qsort(L):
    if len(L) <= 1:
        return L
    return qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1]+\
    qsort([ge for ge in L[1:] if ge >= L[0]])

def quicksorts(ints, left, right):
    key = ints[left]
    while left < right:
        while left < right and ints[right] >= key:
            right -= 1
        if left < right:
            ints[left],ints[right] = ints[right],ints[left]
        else:
            break
        while left < right and ints[left] < key:
            left += 1
        if left < right:
            ints[right], ints[left] = ints[left], ints[right]
        else:
            break
    return left
def fb(n):
        return fb(n-1)+fb(n-2) if n>2 else 1

def quick_sort_standord(ints,left,right):
    if left < right:
        key_index = quicksorts(ints,left,right)
        quick_sort_standord(ints,left,key_index)
        quick_sort_standord(ints,key_index+1,right)

if __name__=="__main__":
    data=[random.random() for x in range(1000)]
    print(len(data))
    a01=x_sort(data)
    a02=y_sort(data)
    a03=z_sort(data)
    tm=time.clock()
    a04=quik_sort(data)
    print('耗时',time.clock()-tm)
    print(len(a04))


    tm = time.clock()
    a04 = qsort(data)
    print('耗时', time.clock() - tm)

    tm = time.clock()
    a05 = quick_sort_standord(data,0,len(data)-1)
    print('耗时', time.clock() - tm)

    fx=lambda n: fx(n-1)+fx(n-2) if n>2 else 1

    for x in range(1,20):
        print(fx(x))

    #print(a01)