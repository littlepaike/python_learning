import copy

"""
测试zip并行迭代
"""
name = ('1', '2', '3')
ages = (12, 12, 123)
jobs = ("a", "b", "c", "d")
for name, age, job in zip(name, ages, jobs):
    print(name, age, job)

'''
浅拷贝和深拷贝
传递不可变对象时，不可变对象里面包含的子对象是可变的。则方法内修改了这个可变对象，源对象也发生了变化
'''


def testCopy():
    a = [10, 20, [30, 40]]
    b = copy.copy(a)
    print("a", a)
    print("b", b)

    b.append(a)
    b[2].append(7)
    print("浅拷贝")
    print("a", a)
    print("b", b)


def testDeepCopy():
    a = [10, 20, [30, 40]]
    b = copy.deepcopy(a)
    print("a", a)
    print("b", b)

    b.append(a)
    b[2].append(7)
    print("浅拷贝")
    print("a", a)
    print("b", b)


testDeepCopy()


