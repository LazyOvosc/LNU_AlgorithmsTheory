def very_first_rule(line: str, position: int):
    if line[position] == 'B':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position + 1, 1


def first_rule(line: str, position: int):
    if line[position] == '1':
        line = line[:position] + '1' + line[position + 1:]
        return line, position + 1, 2


def second_rule(line: str, position: int):
    if line[position] == '1':
        line = line[:position] + '1' + line[position + 1:]
        return line, position + 1, 2
    if line[position] == '+':
        line = line[:position] + '1' + line[position + 1:]
        return line, position + 1, 3


def third_rule(line: str, position: int):
    if line[position] == '1':
        line = line[:position] + '1' + line[position + 1:]
        return line, position + 1, 3
    if line[position] == 'B':
        return line, position - 1, 4


def fourth_rule(line: str, position: int):
    if line[position] == '1':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position - 1, 5


def fifth_rule(line: str, position: int):
    return line, position, -1


def logic():
    position = 0
    line = 'B1111+11B'  # 4 + 2
    rule = 0
    rule_dic = {0: very_first_rule, 1: first_rule, 2: second_rule, 3: third_rule, 4: fourth_rule, 5: fifth_rule}
    while rule != -1:
        line, position, rule = rule_dic[rule](line, position)
    print(line.replace('B', ''))
    print(len(line.replace('B', '')))


logic()