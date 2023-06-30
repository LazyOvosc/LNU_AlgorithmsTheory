import copy


def incorrect_print():
    print('Incorrect')


def correct_print():
    print('Correct')


zero_rule = {
    ('b', 'b'): ['b', 'b', 1, 1, 1]
}
# first symbol, second symbol, first move, second move, direction
first_rule = {
    ('1', '0'): ['1', '0', 0, 1, 1],
    ('1', '1'): ['1', '1', 0, 1, 1],
    ('0', '0'): ['0', '0', 0, 1, 1],
    ('0', '1'): ['0', '1', 0, 1, 1],
    ('1', 'b'): ['1', 'b', 0, -1, 2],
    ('0', 'b'): ['0', 'b', 0, -1, 2]
}
second_rule = {
    ('1', '0'): ['1', '0', 0, 0, 3],
    ('1', '1'): ['1', '1', 1, -1, 2],
    ('0', '0'): ['0', '0', 1, -1, 2],
    ('0', '1'): ['0', '1', 0, 0, 3],
    ('b', 'b'): ['b', 'b', 0, 0, 4]
}
incorrect = {
    ('1', '0'): incorrect_print,
    ('0', '1'): incorrect_print
}
correct = {
    ('b', 'b'): correct_print
}
print()
rules = {
    0: zero_rule,
    1: first_rule,
    2: second_rule,
    3: incorrect,
    4: correct
}

first_check = ['b', '0', '0', '1', '0', 'b']
second_check = ['b', '0', '1', '1', '1', '0', 'b']


def turing(line):
    first_line = copy.deepcopy(line)
    second_line = copy.deepcopy(line)
    first_pos = 0
    second_pos = 0
    rule = 0
    while rule < 3:
        [f_symb, s_symb, f_pos, s_pos, r] = rules[rule][(first_line[first_pos], second_line[second_pos])]
        first_line[first_pos] = f_symb
        second_line[second_pos] = s_symb
        first_pos += f_pos
        second_pos += s_pos
        rule = r
    rules[rule][(first_line[first_pos], second_line[second_pos])]()

turing(first_check)
turing(second_check)

