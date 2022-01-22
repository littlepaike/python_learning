"""
GOF 23种设计模式
"""


class CarFactory:
    def create_car(self, brand):
        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMD()
        elif brand == "比亚迪":
            return BYD()
        else:
            print("未知品牌 无法创建")


class Benz:
    pass


class BMD:
    pass


class BYD:
    pass


factory = CarFactory()
c1 = factory.create_car("奔驰")
c2 = factory.create_car("比亚迪")
