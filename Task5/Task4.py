def f(x):
    return x


def g(x):
    return x + 1


def h(x):
    return x + 2


def superposition(f, g, h):
    def composed(x):
        return f(g(h(x)))
    return composed


fg = superposition(f, g, h)
print(fg(1))