def f(x):
    return x ** 2


def simple_recursion(f, x, n=1):
    if n == 0:
        return x
    else:
        return f(simple_recursion(f, x, n-1))


print(simple_recursion(f, 3, 2))
