# -*- coding:utf-8 -*-
_author_ = 'jackie.ma'


def str2int(s1):
    t = 0
    for i in range(len(s1)):
        t = t+(ord(s1[i])-ord('0'))*10**(len(s1)-i-1)
    return t


if __name__ == "__main__":
    a = '1234987'
    b='lHJKNM'
    print(str2int(a))

    print(sum([10**x[0]*(ord(x[1])-48) for x in enumerate(a[::-1])]))


