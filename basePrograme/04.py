'''
测试zip并行迭代
'''
name = ('1', '2', '3')
ages = (12, 12, 123)
jobs = ("a", "b", "c", "d")
for name, age, job in zip(name, ages, jobs):
    print(name, age, job)
