def zero_rule(line: str, position: int):
    if line[position] == '0':
        line = line[:position] + '0' + line[position + 1:]
        return line, position + 1, 0
    if line[position] == '1':
        line = line[:position] + '1' + line[position + 1:]
        return line, position + 1, 0
    if line[position] == 'B':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position + 1, 1


def first_rule(line: str, position: int):
    if line[position] == '0':
        line = line[:position] + '0' + line[position + 1:]
        return line, position + 1, 1
    if line[position] == '1':
        line = line[:position] + '1' + line[position + 1:]
        return line, position + 1, 1
    if line[position] == 'B':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position - 1, 2


def second_rule(line: str, position: int):
    if line[position] == '0':
        line = line[:position] + '1' + line[position + 1:]
        return line, position - 1, 2
    if line[position] == '1':
        line = line[:position] + '0' + line[position + 1:]
        return line, position - 1, 3
    if line[position] == 'B':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position + 1, 5


def third_rule(line: str, position: int):
    if line[position] == '0':
        line = line[:position] + '0' + line[position + 1:]
        return line, position - 1, 3
    if line[position] == '1':
        line = line[:position] + '1' + line[position + 1:]
        return line, position - 1, 3
    if line[position] == 'B':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position - 1, 4


def fourth_rule(line: str, position: int):
    if line[position] == '0':
        line = line[:position] + '1' + line[position + 1:]
        return line, position + 1, 0
    if line[position] == '1':
        line = line[:position] + '0' + line[position + 1:]
        return line, position - 1, 4
    if line[position] == 'B':
        line = line[:position] + '1' + line[position + 1:]
        return line, position + 1, 0


def fifth_rule(line: str, position: int):
    if line[position] == '1':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position + 1, 5
    if line[position] == 'B':
        return line, position + 1, -1


def logic():
    position = 1
    line = 'B1101B101B'  # 13 + 5
    rule = 0
    rule_dic = {0: zero_rule, 1: first_rule, 2: second_rule, 3: third_rule, 4: fourth_rule, 5: fifth_rule}
    while rule != -1:
        line, position, rule = rule_dic[rule](line, position)
    print(line.replace('B', ''))


logic()
