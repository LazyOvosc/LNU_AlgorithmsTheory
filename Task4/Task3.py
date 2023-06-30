def subtract(a: str, b: str):
    if len(a) < len(b):
        return False
    a = a + '0' + b
    while True:
        if '01' in a:
            a = a.replace('101', '0', 1)
        elif '0' in a:
            a = a.replace('0', '', 1)
        else:
            break
    return a


number = subtract('1111111', '1111')
print(number)
print(len(number))
