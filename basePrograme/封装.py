"""
私有属性和私有方法 ——实现封装
"""


# 测试私有属性
class Employee:
    __company = "fzyy"

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性

    def __work(self):
        '''私有方法'''
        print("好好学习 天天向上")
        print("年龄：{0}".format(self.__age))

    def test(self):
        self.__work()
        print(Employee.__company)


e = Employee("fzy", 18)
print(e.name)
e.test()
# print(e.age)
# print(e._Employee__age)#可以看到私有属性，但是是逻辑上不能查看的
# e._Employee__work() #同上
