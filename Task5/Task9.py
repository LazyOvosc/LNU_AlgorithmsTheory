def simple_recursive_multiplication(x, n):
    if n == 0:
        return 0
    else:
        return x + simple_recursive_multiplication(x, n-1)


print(simple_recursive_multiplication(3, 8))
