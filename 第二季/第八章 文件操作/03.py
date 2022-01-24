a = ['i love u', '尚学堂\n', '百战程序员\n']
b = enumerate(a)
print(a)
print(list(b))

c = [temp.rstrip() + "#" + str(index) for index, temp in enumerate(a)]
print(c)
