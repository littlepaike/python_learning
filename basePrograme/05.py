"""
lambda表达式和匿名函数
"""

f = lambda a, b, c, d: a * b * c * d
print(f(2, 3, 4, 5))

"""
eval函数
"""
s = "print('abcd')"
eval(s)

a = 10
b = 20
dict1 = dict(a=100, b=200)
d = eval("a+b", dict1)
print(d)

"""
递归函数
"""


def test01():
    print("test01")
    test02()


def test02():
    print("test02")


test01()


# 计算阶乘
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


res = factorial(10)
print(res)

"""
nonlacal关键字  用来声明外层的局部变量
global 用来声明全局变量
"""

a = 10
def outer():
    b = 10

    def inner():
        nonlocal b
        print("inner:", b)
        b = 20

        global a
        a = 1000
    inner()
    print("outer b:",b)

outer()
print(a)