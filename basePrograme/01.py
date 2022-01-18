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

# zip
a = [10, 20, 30]
b = [40, 50, 60]
c = [70, 80, 90]
d = zip(a, b, c)
print(d)
print(list(d))

'''
生成器的使用测试
'''
## 元组核心特点：不可变序列
## 元组的访问和处理组都比列表快
## 与整数和字符串一样，可以作为字典的键，列表不可作为字典的键
s = (x * 2 for x in range(5))
print(s)  ##生成器对象只能使用一次
print(tuple(s))

'''
字典
'''
a = {
    'name': 'fzy',
    'age': 18,
    'job': 'programmer'
}
print(a)
print(type(a))

# 通过zip() 创建字典对象
k = ['name', 'age', 'job']
v = ['fzy', '18', 'student']
d = dict(zip(k, v))
print(d)

# fromkeys
a = dict.fromkeys(['a', 'b'])
print(a)

# 字典元素的访问
a = {
    'name': 'fzy',
    'age': 18,
    'job': 'programmer'
}
print(a['name'])

##key不存在可以设置返回自定义
print(a.get('name'))
print(a.get('namea'))  ##不存在可以设置返回自定义
print(a.get('namea', '母鸡啊'))  ##不存在可以设置返回自定义

print(a.items())
print(a.keys())
print(a.values())
print(len(a))

###字典元素的添加修改删除
a['address'] = "hs"
print(a)

'''
序列解包
'''
x, y, z = (20, 30, 10)
print(x)
print(y)
print(z)
