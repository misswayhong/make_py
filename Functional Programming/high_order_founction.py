# 高阶函数
f = abs
def add(x, y, f):
    return f(x) + f(y)

print(add(2, -2, abs))