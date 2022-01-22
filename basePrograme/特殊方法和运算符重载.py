# 测试运算符的重载
class Person:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Person):
            return "{0}_{1}".format(self.name, other.name)
        else:
            return "不是同类对象，不能相加"


p1 = Person("fzt")
p2 = Person("fzy")

x = p1 + p2
print(x)
