from RAM import RAM


numbers = [6, -1, 4, 2, -5, -3, 4]

program = [
    'read 0',
    'load 0',
    'add =1',
    'store 0',
    'sub 0',
    'store *0',  # 5
    'load 0',
    'sub =1',
    'store 0',
    'add =1',
    'store *0',  # 10
    # checking if there are numbers left
    'load *0',
    'sub 0',
    'sub 0',
    'jltz 17',
    'read *0',  # 15
    'jump 38',
    # reading
    'load *0',
    'sub 0',
    'read s',
    'jump 25',  # 20
    # adding to the index
    'load *0',
    'add =1',
    'store *0',
    'jump 11',
    'load s',  # 25
    'jzero 21',
    'jgtz 21',
    'load 0',
    'add = 1',
    'store 0',  # 30
    'load s',
    'add =1',
    'store *0',
    'load 0',
    'sub =1',  # 35
    'store 0',
    'jump 21',
    'load 0',
    'add =1',
    'store 0',
    'write *0',
    'sub =1',
    'store 0',
    'halt'
]

ram = RAM(numbers, program)
ram.execute()
