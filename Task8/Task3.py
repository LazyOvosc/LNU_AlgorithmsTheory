from RAM import RAM

numbers = [4]

program = [
    'read 0',
    'load 0',
    'store 1',
    'sub =1',
    'store 2',
    'load 0',
    'mult 1',
    'store 0',
    'load 2',
    'sub =1',
    'store 2',
    'jgtz 4',
    'write 0',
    'halt'
]

ram = RAM(numbers, program)
ram.execute()
