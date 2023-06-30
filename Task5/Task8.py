def add(x, y):
    if y == 0:
        return x
    elif x == 0:
        return y
    else:
        return add(x+1, y-1)


def g(x):
    return x


def h(x, y, z):
    return z+1


def f(x, y):
    if y == 0:
        return g(x)
    elif y == 1:
        return h(x, 0, x)
    else:
        return h(x, y-1, f(x, y-1))


print(add(3, 5))
print(f(3, 5))
