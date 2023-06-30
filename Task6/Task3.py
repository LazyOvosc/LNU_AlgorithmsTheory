def zero_rule(line: str, position: int):
    if line[position] == 'B':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position + 1, 0
    if line[position] == '1':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position + 1, 1


def first_rule(line: str, position: int):
    if line[position] == 'B':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position + 1, 2
    if line[position] == '1':
        line = line[:position] + '1' + line[position + 1:]
        return line, position + 1, 1


def second_rule(line: str, position: int):
    if line[position] == 'B':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position - 1, 3
    if line[position] == '1':
        line = line[:position] + '1' + line[position + 1:]
        return line, position + 1, 2


def third_rule(line: str, position: int):
    if line[position] == 'B':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position, -1
    if line[position] == '1':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position - 1, 4


def fourth_rule(line: str, position: int):
    if line[position] == 'B':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position, -1
    if line[position] == '1':
        line = line[:position] + '1' + line[position + 1:]
        return line, position - 1, 5


def fifth_rule(line: str, position: int):
    if line[position] == 'B':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position - 1, 6
    if line[position] == '1':
        line = line[:position] + '1' + line[position + 1:]
        return line, position - 1, 5


def sixth_rule(line: str, position: int):
    if line[position] == 'B':
        return line, position, -1
    if line[position] == '1':
        line = line[:position] + '1' + line[position + 1:]
        return line, position - 1, 7


def seventh_rule(line: str, position: int):
    if line[position] == 'B':
        line = line[:position] + 'B' + line[position + 1:]
        return line, position + 1, 0
    if line[position] == '1':
        line = line[:position] + '1' + line[position + 1:]
        return line, position - 1, 7


def logic():
    position = 1
    rule = 0
    line = 'B1111B11B'  # 4 - 2
    rules = {0: zero_rule, 1: first_rule, 2: second_rule, 3: third_rule, 4: fourth_rule, 5: fifth_rule, 6: sixth_rule,
             7: seventh_rule}
    while rule != -1:
        line, position, rule = rules[rule](line, position)
    print(line.replace('B', ''))
    print(len(line.replace('B', '')))


logic()
