"""
单例模式
"""


class MySingleton:
    __obj = None
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self, name):
        if MySingleton.__init_flag:
            self.name = name
            print("init")
            MySingleton.__init_flag = False


a = MySingleton("aa")
b = MySingleton("bb")

print(a)
print(b)
print(a.name)
print(b.name)