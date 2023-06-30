def normal_algorithm(s):
    while True:
        if 'yyx' in s:
            s = s.replace('yyx', 'y', 1)
        elif 'xx' in s:
            s = s.replace('xx', 'y', 1)
        elif 'yyy' in s:
            s = s.replace('yyy', 'x', 1)
        else:
            break
    return s


word = 'xyxxyxyxyxyxyyyxxyyyy'
print(word)
word = normal_algorithm(word)
print(word)
