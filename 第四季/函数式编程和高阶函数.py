from functools import reduce

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sumTest(x, y):
    return x + y


sum = reduce(sumTest, a)
print(sum)


def fn(x, y):
    return x * 10 + y


sum2 = reduce(fn, a)
print(sum2)
