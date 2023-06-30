first_set_of_rules = {
    0: ('B', 'B', 1, 1),
    1: ('B', 'B', 1, 14),
    2: ('B', 'B', 1, 3),
    3: ('B', 'B', -1, 15),
    4: ('B', 'B', 1, 5),
    5: ('B', '1', -1, 6),
    6: ('B', 'B', -1, 7),
    7: ('B', '1', -1, 9),
    8: ('B', '1', 1, 3),
    9: ('B', 'B', -1, 10),
    10: ('B', 'B', 1, 12),
    11: ('B', 'B', 1, 0),
    12: ('B', 'B', 1, 12),
    13: ('B', 'B', 0, -1),
    14: ('B', 'B', 0, -1),
    15: ('B', 'B', -1, 16),
    16: ('B', 'B', 0, -1),
}
second_set_of_rules = {
    0: ('1', 'B', 1, 2),
    1: ('1', 'B', 1, 2),
    2: ('1', '1', 1, 2),
    3: ('1', 'B', 1, 4),
    4: ('1', '1', 1, 4),
    5: ('1', '1', 1, 5),
    6: ('1', '1', -1, 6),
    7: ('1', '1', -1, 8),
    8: ('1', '1', -1, 8),
    9: ('1', '1', -1, 9),
    10: ('1', '1', -1, 11),
    11: ('1', '1', -1, 11),
    12: ('1', 'B', 1, 13),
    13: ('1', 'B', 1, 13),
    14: ('1', 'B', 1, 14),
    15: ('1', 'B', -1, 15),
    16: ('1', 'B', -1, 16)
}


def logic():
    position = 0
    rule = 0
    line = 'B1111111B11B'  # 5 * 2
    while rule != -1:
        if position == len(line):
            line += 'B'
        if position < 0:
            line = 'B' + line
            position = 0
        if line[position] == first_set_of_rules[rule][0]:
            line = line[:position] + first_set_of_rules[rule][1] + line[position + 1:]
            position += first_set_of_rules[rule][2]
            rule = first_set_of_rules[rule][3]
        elif line[position] == second_set_of_rules[rule][0]:
            line = line[:position] + second_set_of_rules[rule][1] + line[position + 1:]
            position += second_set_of_rules[rule][2]
            rule = second_set_of_rules[rule][3]
    print(line.replace('B', ''))
    print(len(line.replace('B', '')))


logic()
