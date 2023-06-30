zero_rule = {
    ('b', 'b', 'b'): ['b', 'b', 'b', 1, 1, 1, 1]
}
first_rule = {
    ('0', '1', 'b'): ['0', '1', '0', 1, 0, 1, 1],
    ('0', '0', 'b'): ['0', '0', '0', 1, 0, 1, 1],
    ('1', '0', 'b'): ['1', '0', '1', 1, 0, 1, 1],
    ('1', '1', 'b'): ['1', '1', '1', 1, 0, 1, 1],
    ('b', '0', 'b'): ['b', '0', 'b', 0, 0, 1, 2],
    ('b', '1', 'b'): ['b', '1', 'b', 0, 0, 1, 2]
}
second_rule = {
    ('b', '0', 'b'): ['b', '0', '0', 0, 1, 1, 2],
    ('b', '1', 'b'): ['b', '1', '1', 0, 1, 1, 2],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, -1, 3]
}
third_rule = {
    ('b', 'b', '0'): ['b', 'b', '0', 0, 0, -1, 3],
    ('b', 'b', '1'): ['b', 'b', '1', 0, 0, -1, 3],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, -1, 4]
}
fourth_rule = {
    ('b', 'b', '0'): ['b', 'b', '0', 0, 0, -1, 4],
    ('b', 'b', '1'): ['b', 'b', '1', 0, 0, -1, 4],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, 1, 5]
}
# region Adding
fifth_rule = {
    ('b', 'b', '0'): ['b', 'b', '0', 0, 0, 1, 5],
    ('b', 'b', '1'): ['b', 'b', '1', 0, 0, 1, 5],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, 1, 6]
}
sixth_rule = {
    ('b', 'b', '0'): ['b', 'b', '0', 0, 0, 1, 6],
    ('b', 'b', '1'): ['b', 'b', '1', 0, 0, 1, 6],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, -1, 7]
}
seventh_rule = {
    ('b', 'b', '0'): ['b', 'b', '1', 0, 0, -1, 7],
    ('b', 'b', '1'): ['b', 'b', '0', 0, 0, -1, 8],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, 1, 10]
}
eighth_rule = {
    ('b', 'b', '0'): ['b', 'b', '0', 0, 0, -1, 8],
    ('b', 'b', '1'): ['b', 'b', '1', 0, 0, -1, 8],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, -1, 9]
}
ninth_rule = {
    ('b', 'b', '0'): ['b', 'b', '1', 0, 0, 1, 5],
    ('b', 'b', '1'): ['b', 'b', '0', 0, 0, -1, 9],
    ('b', 'b', 'b'): ['b', 'b', '1', 0, 0, 1, 5]
}
tenth_rule = {
    ('b', 'b', '1'): ['b', 'b', 'b', 0, 0, 1, 10],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, 0, -1]
}
# endregion Adding
rules = {
    0: zero_rule,
    1: first_rule,
    2: second_rule,
    3: third_rule,
    4: fourth_rule,
    5: fifth_rule,
    6: sixth_rule,
    7: seventh_rule,
    8: eighth_rule,
    9: ninth_rule,
    10: tenth_rule
}


def main():
    first_line = ['b', '1', '1', '0', '1', 'b']
    second_line = ['b', '1', '0', '1', 'b']
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
        if third_pos >= len(third_line):
            while third_pos >= len(third_line):
                third_line.append('b')
        print(third_line)

    result = ''
    for symbol in third_line:
        result += symbol
    result = result.replace('b', '')
    print(result)


main()
