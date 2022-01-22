"""
测试方法的重写
"""


# 继承
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性

    def say_age(self):
        print("我的年龄:", self.__age)

    def say_introduce(self):
        print("我的名字是{0}".format(self.name))


class Student(Person):
    def __init__(self, name, age, score):
        Person.__init__(self, name, age)  # 必须显式的调用父类初始化方法，不然解释器不会调用
        self.score = score

    def say_introduce(self):
        '''重写了父类的 方法'''
        print("报告老师，我的名字是：{0}".format(self.name))


s = Student("fzy", 18, 60)
s.say_age()
s.say_introduce()
print(Student.mro())