def normal_algorithm(s):
    while True:
        if 'yx' in s:
            s = s.replace('yx', 'xy', 1)
        elif 'xy' in s:
            s = s.replace('xy', '', 1)
        else:
            break
    return s


word = 'xyxxyxyxyxyxyyyxxy'
print(word)
word = normal_algorithm(word)
print(word)

#       +----+         +----+
#       |    |    y    |    |
# +-----v----+ <-------+----+
# |          |         |    |
# |     x    |         |    |
# |          |   x,y   |    |
# +----+-----> <-------+----+
#      |               |
#      |               |
#      |               v
#      +---------------+
#              |
#              |
#              v
#             HALT

