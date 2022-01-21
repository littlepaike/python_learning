"""
@property可以将一个方法的调用方式变成属性调用
"""


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print("输入错误，薪水应在1000-50000之间")


emp1 = Employee("fzy", 20000)
print(emp1.salary)
emp1.salary = -2000
print(emp1.salary)

'''
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print("输入错误，薪水应在1000-50000之间")
emp1 = Employee("fzy", 30000)
print(emp1.get_salary())
emp1.set_salary(-20000)
print(emp1.get_salary())
'''
