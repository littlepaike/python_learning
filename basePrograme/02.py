r1 = {
    'name': "fzy",
    'age': 18,
    'salary': 20000,
    'city': '北京'
}

r2 = {
    'name': "fsy",
    'age': 11,
    'salary': 220000,
    'city': '北京2'
}
r3 = {
    'name': "fqy",
    'age': 14,
    'salary': 203000,
    'city': '北京1'
}

tb = [r1, r2, r3]
# 获得第二行人的薪资
print(tb[1].get("salary"))

# 所有人的薪资
for i in range(len(tb)):
    print(tb[i].get("salary"))

# 打印表中所有的数据
for i in range(len(tb)):
    print(tb[i].get("name"), tb[i].get("age"), tb[i].get("salary"), tb[i].get("city"))

'''
集合
'''
a = {233, 12, 2, 'ad'}
print(type(a))

a = {1, 3, 'fzy'}
b = {'he', 'it', 'her'}
# 交集
print(a|b)
