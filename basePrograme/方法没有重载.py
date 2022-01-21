"""
方法没有重载
只用最后一个同名字的
"""
"""
方法的动态性
"""


class Person:
    def work(self):
        print("努力上班")


def play_game(s):
    print("{0}在玩游戏".format(s))


Person.play = play_game

p = Person()
p.work()
p.play()

"""
一切皆是对象
"""

