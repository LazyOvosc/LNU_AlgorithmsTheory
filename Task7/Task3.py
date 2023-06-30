zero_rule = {
    ('b', 'b', 'b'): ['b', 'b', 'b', 1, 1, 1, 1]
}
first_rule = {
    ('1', 'b', 'b'): ['1', '1', '1', 1, 1, 1, 1],
    ('b', 'b', 'b'): ['b', 'b', 'b', -1, -1, -1, 2],
}
second_rule = {
    ('1', '1', '1'): ['1', '1', '1', -1, 0, 1, 3]
}
third_rule = {  # Going to the left
    ('1', '1', 'b'): ['1', '1', '1', 0, -1, 1, 3],
    ('1', 'b', 'b'): ['1', 'b', 'b', -1, 1, 0, 4],
    ('b', '1', 'b'): ['b', '1', 'b', 0, 0, 0, -1]
}
fourth_rule = {  # Going to the right
    ('1', '1', 'b'): ['1', '1', '1', 0, 1, 1, 4],
    ('1', 'b', 'b'): ['1', 'b', 'b', -1, -1, 0, 3],
    ('b', '1', 'b'): ['b', '1', 'b', 0, 0, 0, -1]
}
rules = {
    0: zero_rule,
    1: first_rule,
    2: second_rule,
    3: third_rule,
    4: fourth_rule
}


def main():
    first_line = ['b', '1', '1', '1', 'b']
    second_line = ['b']
    third_line = ['b']
    first_pos = 0
    second_pos = 0
    third_pos = 0
    rule = 0
    while rule != -1:
        f_symb, s_symb, t_symb, f_pos, s_pos, t_pos, r = \
            rules[rule][(first_line[first_pos], second_line[second_pos], third_line[third_pos])]
        first_line[first_pos] = f_symb
        second_line[second_pos] = s_symb
        third_line[third_pos] = t_symb
        first_pos += f_pos
        second_pos += s_pos
        third_pos += t_pos
        rule = r
        if first_pos == len(first_line):
            first_line.append('b')
        if second_pos == len(second_line):
            second_line.append('b')
        if third_pos == len(third_line):
            third_line.append('b')

    result = ''
    for symbol in third_line:
        result += symbol
    result = result.replace('b', '')
    print(result)
    print(len(result))


main()
