def superposition(f, g):
    def composed(x):
        return f(g(x))
    return composed


def f(x):
    return x + 1


def g(x):
    return x + 2


fg = superposition(f, g)
print(fg(1))
