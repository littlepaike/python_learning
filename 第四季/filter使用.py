def is_odd(n):
    return n % 2 == 1


L = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(L))
# 一个序列中的空字符串删掉
a = ['A', '', 'B', None, 'C', ' ']


def not_empty(s):
    return s and s.strip()


L = filter(not_empty, a)
print(list(L))

sort_list = sorted([42, 422, 42, 1])
print('默认升序', sort_list)

# plus
sort_list = sorted([42, 422, -100, 42, 1], key=abs)
print('绝对值升序', sort_list)
