# -*- coding:utf-8 -*- 
_author_ = 'jackie.ma'

def str_cat(str1,str2):
    return  str1+str2
class father():
    def __init__(self,name):
        self.name=name
    def getn(self):
        return self.name
    def setn(self,name):
        self.name=name
    def deln(self):
        del self.name
    x=property(getn,setn,deln)

class son(father):
    def __init__(self,name):
        self.name=name
        super(son, self).__init__(name + 'fat')
    def ppn(self):
        print('son-',self.name,'fata',super(son,self).x)

class x_cx:

    def __init__(self,name):
        self.name="go"
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name+"_str"
    def get_name(self):
        return  self.name
    def set_name(self,name):
        self.name=name
    def del_name(self):
        del self.name
    x=property(get_name,set_name,del_name,'IamNmaX')


class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name='tom', salary=10):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print(        "Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print(        "Name : ", self.name, ", Salary: ", self.salary)


if __name__=="__main__":
    cx=x_cx("YES or NO")
    cx.x='Jakcie'
    print(cx.x)
    # print(str(cx))



    # a=input('a---:')
    # b=input('b---:')
    # print(str_cat(a,b))

    tom=Employee()
    jack=Employee('Jack',33)

    tom.displayCount()
    jack.displayCount()

    tom=son('TOMMY')
    tom.ppn()


