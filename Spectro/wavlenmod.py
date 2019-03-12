# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'
from math import sin,pi
import matplotlib.pyplot as plt
def peak(x):
    return sin(x)**2

###TDLAS论文###http://www.docin.com/p-1441813150.html
####http://www.docin.com/p-1437135028.html
###http://www.docin.com/p-1421655500.html
###http://www.doc88.com/p-5486803491608.html
###http://www.doc88.com/p-5969583065105.html
if __name__=='__main__':
    vb=98
    w=[(x-50)/10 for x in range(100)]
    y=[peak(x) for x in w]
    z=[x/pi for x in w]
    plt.figure()
    plt.plot(z,y,'*-r')
    #plt.plot(z,z,'*-g')
    plt.grid()
    plt.show()
