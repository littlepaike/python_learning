"""
封装
继承
多态
"""


# 继承
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #私有属性

    def say_age(self):
        print("我的年龄18")


class Student(Person):
    def __init__(self, name, age, score):
        Person.__init__(self, name, age)  # 必须显式的调用父类初始化方法，不然解释器不会调用
        self.score = score


#
# print(Student.mro())
s = Student("fzy", 18, 60)
s.say_age()  # 父类中方法子类可以用
print(s.name)

