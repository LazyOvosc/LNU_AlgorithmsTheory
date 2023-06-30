from RAM import RAM


numbers = [6, 1, 4, 2, 5, 3, 4]

program = [
    'read 0',
    'load 0',
    'add =1',
    'store *0',  # 3
    # checking if there are numbers left
    'load *0',
    'sub 0',
    'sub 0',
    'jltz 10',
    'read *0',
    'jump 17',  # 9
    # reading
    'load *0',
    'sub 0',
    'read s',  # 12
    # adding to the index
    'load *0',
    'add =1',
    'store *0',
    'jump 4',  # 16
    # adding new variable
    'load 0',
    'add =1',
    'store 0',
    'sub =1',
    'mult 0',
    'store *0',  # 22
    # sorting
    'load *0',
    'rem 0',
    'jzero 33',
    'jltz 37',
    'sub 0',
    'add =1',
    'jzero 33',
    'load *0',
    'rem 0',
    'grswap s',
    'load *0',  # 33
    'sub =1',
    'store *0',
    'jgtz 23',

    # printing
    'load 0',
    'sub =1',
    'jgtz 41',
    'halt',
    'write s',
    'jump 38'
]

RAM = RAM(numbers, program)
RAM.execute()
