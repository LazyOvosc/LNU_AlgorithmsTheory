parity_check0 = {
    '1': ['1', 1, 0],
    '0': ['0', 1, 0],
    'x': ['x', -1, 1]
}
parity_check1 = {
    '1': ['b', 1, 2],
    '0': ['0', -1, 1],
    'x': ['x', 1, 5]
}
parity_check2 = {
    '0': ['0', 1, 2],
    'b': ['b', 1, 2],
    'x': ['x', 1, 3]
}
parity_check3 = {
    '1': ['1', 1, 3],
    'b': ['1', -1, 4]
}
parity_check4 = {
    '1': ['1', -1, 4],
    'x': ['x', -1, 5]
}
parity_check5 = {
    '0': ['0', -1, 5],
    'b': ['b', -1, 5],
    '1': ['1', 0, 1],
    'x': ['x', 1, 6]
}
parity_check6 = {
    '0': ['0', 1, 6],
    'b': ['b', 1, 6],
    'x': ['x', 1, 7]
}
parity_check7 = {
    '1': ['1', 1, 7],
    'b': ['b', -1, 8],
    '0': ['0', -1, 8]
}
parity_check8 = {
    '1': ['0', -1, 9]
}
parity_check9 = {
    'x': ['x', 0, False],
    '0': ['0', 0, False],
    '1': ['1', 0, 10]
}
parity_check10 = {
    '1': ['1', -1, 10],
    'x': ['x', 1, 11],
    '0': ['0', 1, 11],
}
parity_check11 = {
    '1': ['0', 1, 12]
}
parity_check12 = {
    '0': ['0', 0, 13],
    '1': ['1', 0, 7]
}
parity_check13 = {
    '0': ['0', 1, 13],
    'b': ['b', -1, 14]
}
parity_check14 = {
    '0': ['b', -1, 15]
}
parity_check15 = {
    '0': ['0', -1, 15],
    'x': ['x', -1, 16]
}
parity_check16 = {
    'b': ['1', 1, 17],
    '1': ['1', -1, 16],
    '0': ['0', -1, 16]
}
parity_check17 = {
    '1': ['1', 1, 17],
    '0': ['0', 1, 17],
    'x': ['x', 1, 18]
}
parity_check18 = {
    'b': ['b', -1, 19],
    '0': ['0', 0, 13]
}
parity_check19 = {
    'x': ['x', -1, 20]
}
parity_check20 = {
    '1': ['1', -1, 20],
    '0': ['0', -1, 20],
    'x': ['x', 1, True]
}


parity_rules = {
    0: parity_check0,
    1: parity_check1,
    2: parity_check2,
    3: parity_check3,
    4: parity_check4,
    5: parity_check5,
    6: parity_check6,
    7: parity_check7,
    8: parity_check8,
    9: parity_check9,
    10: parity_check10,
    11: parity_check11,
    12: parity_check12,
    13: parity_check13,
    14: parity_check14,
    15: parity_check15,
    16: parity_check16,
    17: parity_check17,
    18: parity_check18,
    19: parity_check19,
    20: parity_check20
}
