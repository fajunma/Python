# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'
from math import sin,pi
import matplotlib.pyplot as plt
def peak(x):
    return sin(x)**2


if __name__=='__main__':
    w=[(x-50)/10 for x in range(100)]
    y=[peak(x) for x in w]
    z=[x/pi for x in w]
    plt.figure()
    plt.plot(z,y,'*-r')
    #plt.plot(z,z,'*-g')
    plt.grid()
    plt.show()
