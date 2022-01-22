# 测试组合

class A:
    print("aaaaa")


class B:
    def __init__(self, a):
        self.a = a


b = B(A())
