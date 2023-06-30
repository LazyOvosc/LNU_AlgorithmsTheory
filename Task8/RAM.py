import copy


class RAM:
    def __init__(self, input_line: list, command_line: list[str]):
        self.program = copy.deepcopy(command_line)
        self.input_line = copy.deepcopy(input_line)
        self.memory = [-1 for _ in range(len(input_line))]
        self.output_line = []
        self.summ = 0

    def pos_checker(self, pos: str):
        if pos.startswith('s'):
            return self.summ
        elif pos.startswith('*s'):
            while len(self.memory) <= self.summ:
                self.memory.append(-1)
            return self.memory[self.summ]
        elif pos.startswith('*'):
            while len(self.memory) <= int(pos[1:]):
                self.memory.append(-1)
            return self.memory[int(pos[1:])]
        else:
            return int(pos)

    def value_checker(self, value: str):
        if value.startswith('s'):
            return self.summ
        elif value.startswith('='):
            return int(value[1:])
        else:
            return self.memory[int(value)]

    def LOAD(self, memory_pos: str):
        if memory_pos.startswith('='):
            self.summ = int(memory_pos[1:])
            return
        memory_pos = self.pos_checker(memory_pos)
        while len(self.memory) <= memory_pos:
            self.memory.append(-1)
        self.summ = self.memory[memory_pos]

    def STORE(self, memory_pos: str):
        memory_pos = self.pos_checker(memory_pos)
        while len(self.memory) <= memory_pos:
            self.memory.append(-1)
        self.memory[memory_pos] = self.summ

    def ADD(self, memory_pos: str):
        value = self.value_checker(memory_pos)
        self.summ += value

    def SUB(self, memory_pos: str):
        value = self.value_checker(memory_pos)
        self.summ -= value

    def MULT(self, memory_pos: str):
        value = self.value_checker(memory_pos)
        self.summ *= value

    def DIV(self, memory_pos: str):
        value = self.value_checker(memory_pos)
        self.summ //= value

    def REM(self, memory_pos: str):
        value = self.value_checker(memory_pos)
        self.summ %= value

    def READ(self, line_pos: str):
        line_pos = self.pos_checker(line_pos)
        self.memory[line_pos] = self.input_line[line_pos]

    def WRITE(self, memory_pos: str):
        memory_pos = self.pos_checker(memory_pos)
        while len(self.memory) <= memory_pos:
            self.memory.append(-1)
        self.output_line.append(self.memory[memory_pos])

    def JUMP(self, line_pos: str):
        line_pos = int(line_pos)
        self.summ = self.summ  # do nothing
        return line_pos

    def JGTZ(self, line_pos: str, i: int):
        line_pos = int(line_pos)
        if self.summ > 0:
            return line_pos
        else:
            return i + 1

    def GRSWAP(self, memory_pos: str):
        pos = self.pos_checker(memory_pos)
        if self.memory[pos] < self.memory[pos + 1]:
            self.memory[pos], self.memory[pos + 1] = self.memory[pos + 1], self.memory[pos]

    def JLTZ(self, line_pos: str, i: int):
        line_pos = int(line_pos)
        if self.summ < 0:
            return line_pos
        else:
            return i + 1

    def JZERO(self, line_pos: str, i: int):
        line_pos = int(line_pos)
        if self.summ == 0:
            return line_pos
        else:
            return i + 1

    def HALT(self):
        self.summ = self.summ  # do nothing
        return None

    def execute(self):
        i = 0
        trans = False
        while True:
            a = self.program[i]
            if self.program[i].startswith('load'):
                self.LOAD(self.program[i][5:])
            elif self.program[i].startswith('store'):
                self.STORE(self.program[i][6:])
            elif self.program[i].startswith('add'):
                self.ADD(self.program[i][4:])
            elif self.program[i].startswith('sub'):
                self.SUB(self.program[i][4:])
            elif self.program[i].startswith('mult'):
                self.MULT(self.program[i][5:])
            elif self.program[i].startswith('div'):
                self.DIV(self.program[i][4:])
            elif self.program[i].startswith('rem'):
                self.REM(self.program[i][4:])
            elif self.program[i].startswith('read'):
                self.READ(self.program[i][5:])
            elif self.program[i].startswith('write'):
                self.WRITE(self.program[i][6:])
            elif self.program[i].startswith('grswap'):
                self.GRSWAP(self.program[i][7:])
            elif self.program[i].startswith('jump'):
                print(self.memory, '| ', self.program[i], f'| summ = {self.summ}')
                i = self.JUMP(self.program[i][5:])
                i -= 1
                trans = True
            elif self.program[i].startswith('jgtz'):
                print(self.memory, '| ', self.program[i], f'| summ = {self.summ}')
                i = self.JGTZ(self.program[i][5:], i)
                i -= 1
                trans = True
            elif self.program[i].startswith('jltz'):
                print(self.memory, '| ', self.program[i], f'| summ = {self.summ}')
                i = self.JLTZ(self.program[i][5:], i)
                i -= 1
                trans = True
            elif self.program[i].startswith('jzero'):
                print(self.memory, '| ', self.program[i], f'| summ = {self.summ}')
                i = self.JZERO(self.program[i][6:], i)
                i -= 1
                trans = True
            elif self.program[i].startswith('halt'):
                self.HALT()
                print(self.output_line)
                break
            if trans:
                trans = False
            else:
                print(f'{self.memory} | {self.program[i]} | summ = {self.summ} | {i}')
            i += 1
