a = [10, 20, 30, 40, 50, 60]
result = a[:]
print(result)

# 元组

a = (20, 10, 30, 9, 8)
print(a[3])

# 元组切片
a = tuple("abcdefghijklmnopqrstuvwxyz")
print(a)
print(a[1:10:2])
print(a[::-1])
print(max(a))


#zip
a = [10,20,30]
b = [40,50,60]
c = [70,80,90]
d = zip(a,b,c)
print(d)
print(list(d))