# -*- coding: utf-8 -*-

# map()和reduce()函数
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


# 输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']
L1 = ['adam', 'LISA', 'barT']


def fun2(x):
    return x.capitalize()


L2 = list(map(fun2, L1))  # 把函数作用在序列每一个元素上
print(L2)


#  Python提供的sum()函数可以接受一个list并求和，
# 请编写一个prod()函数，
# 可以接受一个list并利用reduce()求积：



def prod(s):
    from functools import reduce

    def fn(x, y):
        return x*y
    return reduce(fn, s)


s = [3, 5, 7, 9]
print(prod(s))
print(prod([1, 2, 3]))










