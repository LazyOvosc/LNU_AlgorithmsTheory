secondrule0 = {
    '0': ['0', 1, 0],
    '1': ['1', -1, 1],
}
secondrule1 = {
    '0': ['q', 1, 2],
}
secondrule2 = {
    '1': ['1', 1, 2],
    '0': ['q', -1, 3],
    'x': ['x', 1, 11],
}
secondrule3 = {
    '1': ['0', 1, 4],
    '0': ['0', -1, 3],
    'q': ['0', 1, 9],
}
secondrule4 = {
    '0': ['0', 1, 4],
    'q': ['q', 1, 5],
}
secondrule5 = {
    '0': ['0', 1, 5],
    '1': ['1', 1, 5],
    'x': ['x', 1, 6],
}
secondrule6 = {
    'b': ['1', 0, 7],
    '1': ['1', 1, 6],
}
secondrule7 = {
    '1': ['1', -1, 7],
    'x': ['x', -1, 8],
}
secondrule8 = {
    '1': ['1', -1, 8],
    '0': ['0', -1, 8],
    'q': ['q', -1, 3],
}
secondrule9 = {
    '0': ['0', 1, 9],
    'q': ['0', 1, 10],
}
secondrule10 = {
    '0': ['0', -1, True],
    '1': ['1', -1, True],
    'x': ['x', -1, False],
}
secondrule11 = {
    '0': ['0', -1, 11],
    '1': ['1', -1, 11],
    'q': ['0', 0, False],
}
second_rules = {
    0: secondrule0,
    1: secondrule1,
    2: secondrule2,
    3: secondrule3,
    4: secondrule4,
    5: secondrule5,
    6: secondrule6,
    7: secondrule7,
    8: secondrule8,
    9: secondrule9,
    10: secondrule10,
    11: secondrule11,
}