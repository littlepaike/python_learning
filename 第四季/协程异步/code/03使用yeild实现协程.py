import time


def A():
    while True:
        print('-------A--------')
        yield
        print("A")
        time.sleep(0.5)


def B(c):
    while True:
        print('--------B--------')
        c.__next__()
        print("B")
        time.sleep(0.5)


a = A()  # 生成一个生成器对象
B(a)
#
# def a():
#     for i in range(10):
#         a = i
#         yield a
#
#
# print(list(a()))
