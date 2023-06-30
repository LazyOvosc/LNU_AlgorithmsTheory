zero_rule = {
    '0': ('0', 1, 1)
}
first_rule = {
    '0': ('0', 1, 1),
    '1': ('1', 1, 1),
    '2': ('2', 1, 1),
    '3': ('3', 1, 1),
    '4': ('4', 1, 1),
    '5': ('5', 1, 1),
    '6': ('6', 1, 1),
    '7': ('7', 1, 1),
    '8': ('8', 1, 1),
    '9': ('9', 1, 1),
    'B': ('B', 1, 2)
}
second_rule = {
    'B': ('B', 1, 2),
    '1': ('B', -1, 3),
    '0': ('B', 0, -1)
}
third_rule = {
    'B': ('B', -1, 3),
    '0': ('1', 1, 1),
    '1': ('2', 1, 1),
    '2': ('3', 1, 1),
    '3': ('4', 1, 1),
    '4': ('5', 1, 1),
    '5': ('6', 1, 1),
    '6': ('7', 1, 1),
    '7': ('8', 1, 1),
    '8': ('9', 1, 1),
    '9': ('0', -1, 3)
}


def logic():
    position = 0
    rule = 0
    line = '0B111110'  # 5
    print(len(line.replace('B', '').replace('0', '')))
    while rule != -1:
        if position < 0:
            position = 0
            line = '0' + line
        temp_position = position
        if rule == 0:
            rule, position = zero_rule[line[position]][2], position + zero_rule[line[position]][1]
            line = line[:temp_position] + zero_rule[line[temp_position]][0] + line[temp_position + 1:]
        elif rule == 1:
            rule, position = first_rule[line[position]][2], position + first_rule[line[position]][1]
            line = line[:temp_position] + first_rule[line[temp_position]][0] + line[temp_position + 1:]
        elif rule == 2:
            rule, position = second_rule[line[position]][2], position + second_rule[line[position]][1]
            line = line[:temp_position] + second_rule[line[temp_position]][0] + line[temp_position + 1:]
        elif rule == 3:
            rule, position = third_rule[line[position]][2], position + third_rule[line[position]][1]
            line = line[:temp_position] + third_rule[line[temp_position]][0] + line[temp_position + 1:]
    print(line.replace('B', ''))


logic()
