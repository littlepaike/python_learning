# 测试try except else
try:
    a = input("输入一个被除数:")
    b = input("输入一个除数:")
    c = float(a) / float(b)
except BaseException as e:
    print(e)
else:
    print(c)