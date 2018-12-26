# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'
#考虑第五名海盗，当他能做出方案时，此方案必定能通过，也最有利于他，因此，当第四名海盗做出方案时，只要不是（0,100），第五名一定反对，而如果（0,100），第五名可以赞成（毕竟有人聊天挺好）
#所以只要满足最大利益他们并不想多杀人；
##4号提出（0，100）最优结果能不能活，过半数包括半数吗？
import functools

def allocation(n):
    #本次代码是过半数（包括半数）通过
    #本次代码只要利益最大海盗并不想多杀人
    #是否过半数需要在判断中是否小于等于
    #是否有乱杀人的可能，就在于剩下两个人的时候是否最后一个接受【0，100】
    if n<=2:
        result=[[0,0],[1,100]]
        print(result)
        return result
    else:
        need_support_nums=n/2-1#不包括自己
        tmp=allocation(n-1)#上一次的分配结果
        tmp=sorted(tmp,key=lambda x:x[1])#按照分配金额排序

        for i,x in enumerate(tmp):
            if i<need_support_nums:
                #print('suppt',support_nums)
                x[1]=x[1]+1
            else:
                x[1]=0
        tmp.append([n-1,100-functools.reduce(lambda x,y:x+y,[x[1] for x in tmp])])
        tmp=sorted(tmp,key=lambda x:x[0])
        print(tmp)
        return tmp


if __name__=="__main__":
   allocation(10)


