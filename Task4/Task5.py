def multiply(a: str, b: str):
    a = a + '*' + b
    while True:
        print(a)
        if '*11' in a:
            a = a.replace('*11', 'T*1', 1)
        elif '*1' in a:
            a = a.replace('*1', 'T', 1)
        elif '1T' in a:
            a = a.replace('1T', 'T1F', 1)
        elif 'FT' in a:
            a = a.replace('FT', 'TF', 1)
        elif 'F1' in a:
            a = a.replace('F1', '1F', 1)
        elif 'T1' in a:
            a = a.replace('T1', 'T', 1)
        elif 'TF' in a:
            a = a.replace('TF', 'F', 1)
        elif 'F' in a:
            a = a.replace('F', '1', 1)
        else:
            break

    return a


number = multiply('11', '111')
print(number)
print(len(number))
