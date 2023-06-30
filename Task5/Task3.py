def f(x):
    return 0


def g(x):
    return x + 1


def superposition(f, g, x, n=1):
    if n == 0:
        return f(x)
    else:
        return superposition(f, g, g(x), n-1)


x = 2
fg = superposition(f, g, x)
gf = superposition(g, f, x)
gg = superposition(g, g, x)

print(fg, gf, gg)
print(f(g(x)), g(f(x)), g(g(x)))
