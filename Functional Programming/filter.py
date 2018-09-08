# filter()函数也和map()类似，也接收一个函数和一个数列
# 不同的是，filter把传入的函数一次作用于每个元素，然后根据
# 返回值是True还是False来决定是否保留该元素（返回为惰性数列）

# 判断回数，并用filter()筛选出来


def fn(n):
    return str(n) == str(n)[::-1]


outer = list(filter(fn, range(1, 100)))

print(outer)

