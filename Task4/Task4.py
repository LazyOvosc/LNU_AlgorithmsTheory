def add(a: str, b: str):
    a = a + '0' + b
    while True:
        if '01' in a:
            a = a.replace('01', '10', 1)
        elif '0' in a:
            a = a.replace('0', '', 1)
        else:
            break
    return a


number = add('11', '1')
print(number)
print(len(number))
