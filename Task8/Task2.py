from RAM import RAM

numbers = [1, 15, 0]

program = [
    # read first number
    'read 0',
    'load 0',
    # check first number
    'sub =1',
    'jzero 5',
    'jump 44',  # wrong number
    # read second number
    'read 1',  # 5
    'load 1',
    # check second number
    'sub =1',
    'jzero 37',
    'sub =1',
    'jzero 37',  # 10
    'load 1',
    'sub 1',
    'add =2',
    'store 0',
    'mult 0',  # 15
    'sub =1',
    'store 2',
    'load 0',
    'sub 0',
    'add =2',  # 20
    'store 3',
    'load 3',
    'mult =2',
    'store 3',
    'load 2',  # 25
    'sub =1',
    'store 2',
    'jgtz 22',
    'load 3',
    'sub 1',  # 30
    'jzero 37',
    'jltz 44',
    'load 0',
    'sub 0',
    'add =1',  # 35
    'jump 14',
    'load 0',
    'sub 0',
    'add =1',
    'store 0',  # 40
    # check third number
    'read 2',
    'load 2',
    'jzero 49',
    'load 0',
    'sub 0',  # 45
    'store 3',
    'write 3',
    'halt',
    'write 0',
    'halt'  # 50
]

ram = RAM(numbers, program)
ram.execute()
