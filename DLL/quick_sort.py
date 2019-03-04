#!/usr/bin/env python


def f(lst):
    if len(lst)<=1:
        return lst
    else:
        m=[lst[0]]
        l=[]
        r=[]
        for x in  lst[1:]:
            if x<=lst[0]:
                l.append(x)
            else:
                r.append(x)
        return f(l)+m+f(r)


a=[2,4,1,0,9,7,6,9,5,1,0,8]
print(f(a))
print('erfenfa')

