def smart_print(lst, pos: int):
    res = ''
    for i in range(len(lst)):
        if i == pos:
            res += '\033[31m' + str(lst[i]) + '\033[0m'  # Add ANSI escape sequence for red color
        else:
            res += str(lst[i])
    return res


# region First Line
zero_rule = {
    ('0', 'b', 'b'): ['0', 'b', 'b', 1, 0, 0, 0],
    ('1', 'b', 'b'): ['1', 'b', 'b', 1, 0, 0, 0],
    ('b', 'b', 'b'): ['b', 'b', 'b', -1, 0, 0, 1]
}
first_rule = {
    ('0', 'b', 'b'): ['1', 'b', 'b', -1, 0, 0, 1],
    ('1', 'b', 'b'): ['0', 'b', 'b', 1, 0, 0, 2],
    ('b', 'b', 'b'): ['b', 'b', 'b', 1, 0, 0, 5]
}
second_rule = {
    ('0', 'b', 'b'): ['0', 'b', 'b', 1, 0, 0, 2],
    ('1', 'b', 'b'): ['1', 'b', 'b', 1, 0, 0, 2],
    ('b', 'b', 'b'): ['b', 'b', 'b', 1, 0, 0, 3]
}
third_rule = {
    ('1', 'b', 'b'): ['1', 'b', 'b', 1, 0, 0, 3],
    ('b', 'b', 'b'): ['1', 'b', 'b', -1, 0, 0, 4]
}
fourth_rule = {
    ('1', 'b', 'b'): ['1', 'b', 'b', -1, 0, 0, 4],
    ('b', 'b', 'b'): ['b', 'b', 'b', -1, 0, 0, 1]
}
fifth_rule = {
    ('1', 'b', 'b'): ['b', 'b', 'b', 1, 0, 0, 5],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, 0, 6]
}
# endregion First Line
# region Second Line
sixth_rule = {
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 1, 0, 7]
}
seventh_rule = {
    ('b', '0', 'b'): ['b', '0', 'b', 0, 1, 0, 7],
    ('b', '1', 'b'): ['b', '1', 'b', 0, 1, 0, 7],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, -1, 0, 8]
}
eighth_rule = {
    ('b', '0', 'b'): ['b', '1', 'b', 0, -1, 0, 8],
    ('b', '1', 'b'): ['b', '0', 'b', 0, 1, 0, 9],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 1, 0, 12]
}
ninth_rule = {
    ('b', '0', 'b'): ['b', '0', 'b', 0, 1, 0, 9],
    ('b', '1', 'b'): ['b', '1', 'b', 0, 1, 0, 9],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 1, 0, 10]
}
tenth_rule = {
    ('b', '1', 'b'): ['b', '1', 'b', 0, 1, 0, 10],
    ('b', 'b', 'b'): ['b', '1', 'b', 0, -1, 0, 11]
}
eleventh_rule = {
    ('b', '1', 'b'): ['b', '1', 'b', 0, -1, 0, 11],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, -1, 0, 8]
}
twelfth_rule = {
    ('b', '1', 'b'): ['b', 'b', 'b', 0, 1, 0, 12],
    ('b', 'b', 'b'): ['b', 'b', 'b', 1, 0, 0, 13]
}
# endregion Second Line
thirteenth_rule = {
    ('1', 'b', 'b'): ['1', 'b', 'b', 1, 0, 0, 13],
    ('b', 'b', 'b'): ['0', 'b', 'b', -1, 0, 0, 14]
}
fourteenth_rule = {
    ('1', 'b', 'b'): ['1', 'b', 'b', -1, 0, 0, 14],
    ('b', 'b', 'b'): ['b', 'b', 'b', 1, 1, 0, 15]
}
fifteenth_rule = {
    ('1', '1', 'b'): ['1', '1', 'b', 1, 1, 0, 15],
    ('1', 'b', 'b'): ['1', 'b', 'b', -1, -1, 0, 16],
    ('0', 'b', 'b'): ['0', 'b', 'b', -1, -1, 0, 16],
    ('0', '1', 'b'): ['0', '1', 'b', 0, 0, 0, 19],
}
sixteenth_rule = {
    ('1', '1', 'b'): ['b', '1', 'b', -1, -1, 0, 16],
    ('b', 'b', 'b'): ['b', 'b', '1', 0, 0, 1, 18]
}
seventeenth_rule = {
    ('b', '1', 'b'): ['b', '1', 'b', 0, -1, -1, 17],
    ('b', 'b', '1'): ['b', 'b', '1', 0, 0, -1, 17],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, 1, 18]
}
eighteenth_rule = {
    ('b', 'b', 'b'): ['b', 'b', 'b', 1, 0, 0, 18],
    ('1', 'b', 'b'): ['1', 'b', 'b', 0, 1, 0, 15],
    ('0', 'b', 'b'): ['0', 'b', 'b', 0, 0, 0, 19]
}
nineteenth_rule = {
    ('0', 'b', 'b'): ['0', 'b', 'b', 1, 0, 0, 19],
    ('0', '1', 'b'): ['0', '1', 'b', 1, 1, 0, 19],
    ('b', '1', 'b'): ['b', '1', 'b', 0, 1, 0, 19],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, -1, 20]
}
twentieth_rule = {
    ('b', 'b', '1'): ['b', 'b', '1', 0, 0, -1, 20],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, 1, 21]
}
twenty_first_rule = {
    ('b', 'b', '1'): ['b', 'b', '1', 0, 0, 1, 21],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, -1, 22]
}
twenty_second_rule = {
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, 0, 26],
    ('b', 'b', '1'): ['b', 'b', 'b', 0, 0, -1, 23]
}
twenty_third_rule = {
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, -1, 24],
    ('b', 'b', '1'): ['b', 'b', '1', 0, 0, -1, 23]
}
twenty_fourth_rule = {
    ('b', 'b', 'b'): ['b', 'b', '1', 0, 0, 1, 25],
    ('b', 'b', '0'): ['b', 'b', '1', 0, 0, 1, 25],
    ('b', 'b', '1'): ['b', 'b', '0', 0, 0, -1, 24]
}
twenty_fifth_rule = {
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, 1, 21],
    ('b', 'b', '0'): ['b', 'b', '0', 0, 0, 1, 25],
    ('b', 'b', '1'): ['b', 'b', '1', 0, 0, 1, 25]
}
twenty_sixth_rule = {
    ('b', 'b', 'b'): ['b', 'b', 'b', -1, 0, 0, 27],
}
twenty_seventh_rule = {
    ('0', 'b', 'b'): ['b', 'b', 'b', -1, 0, 0, 27],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, 0, -1],
    ('1', 'b', 'b'): ['1', 'b', 'x', 0, 0, 1, 28]
}
twenty_eighth_rule = {
    ('1', 'b', 'b'): ['b', 'b', '1', -1, 0, 1, 28],
    ('b', 'b', 'b'): ['b', 'b', 'b', 0, 0, 0, -1]
}
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
    10: tenth_rule,
    11: eleventh_rule,
    12: twelfth_rule,
    13: thirteenth_rule,
    14: fourteenth_rule,
    15: fifteenth_rule,
    16: sixteenth_rule,
    17: seventeenth_rule,
    18: eighteenth_rule,
    19: nineteenth_rule,
    20: twentieth_rule,
    21: twenty_first_rule,
    22: twenty_second_rule,
    23: twenty_third_rule,
    24: twenty_fourth_rule,
    25: twenty_fifth_rule,
    26: twenty_sixth_rule,
    27: twenty_seventh_rule,
    28: twenty_eighth_rule
}


def main():
    first_line = ['0', '1', '0', '0', '0', '0', '1', '1', '1']
    second_line = ['b', '0', '1', '1', '0', '1']
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
        if third_pos < 0:
            third_line.insert(0, 'b')
            third_pos = 0
        if first_pos < 0:
            first_line.insert(0, 'b')
            first_pos = 0
        if rule > 12:
            print('', end='')
    result = ''
    for symbol in third_line:
        result += symbol
    result = result.replace('b', '')
    print(result)


main()
