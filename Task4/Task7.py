def remove(a: str):
    while True:
        if '  ' in a:
            a = a.replace('  ', ' ', 1)
        else:
            break
    return a


line = 'abc    ac  ac ab'
print(remove(line))
