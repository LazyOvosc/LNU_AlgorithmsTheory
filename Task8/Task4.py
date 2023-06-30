from RAM import RAM

numbers = [3, 1, 2, 3]

program = [
    'read s',
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
    'halt'
]

ram = RAM(numbers, program)
ram.execute()
