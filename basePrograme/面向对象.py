"""
python支持面向过程 面向对象 函数式变成等多种编成范式
"""


# 测试类方法classmethod

class Student:
    company = "fzy"  # 类属性

    @classmethod
    def printCompany(cls):
        print(cls.company)
        # print(self.name) #类方法和静态方法中，不能调用实例变量实例方法


# Student.printCompany()

a = Student()
a.printCompany()


# 静态方法   定义和类完全无关的方法  不操作属性——只是因为通过类去访问
class Student2:
    company = "fzy"

    @staticmethod
    def add(a, b):
        print(a, b, a + b)
        return a + b


"""
析构方法 __del__测试
"""


class Persion:

    def __del__(self):
        print("销毁对象{0}".format(self))


p1 = Persion()
p2 = Persion()
del p2
print("程序结束")

"""
__call__方法和可调用对象
"""


class SalaryAccount:
    '''工资计算类'''

    def __call__(self, salary):
        print("算工资")
        yearSalary = salary * 12
        daySalary = salary // 22.5
        hourSalary = daySalary // 8

        return dict(yearSalary=yearSalary,
                    monthSalary=salary,
                    daySalary=daySalary,
                    hourSalary=hourSalary)


s = SalaryAccount()
print(s(30000))
