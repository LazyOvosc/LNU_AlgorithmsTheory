def predecessor(x):
    return x - 1


def subtract(x, y):
    if y == 0:
        return x
    else:
        return subtract(predecessor(x), predecessor(y))


print(subtract(8, 3))
