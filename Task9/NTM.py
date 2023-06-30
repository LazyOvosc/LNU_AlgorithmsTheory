from copy import deepcopy
from parityCheck import parity_rules
from firstRules import first_rules
from secondRules import second_rules
from sumEqualityRules import sum_rules


def smart_print(pos: int, rule: int, numbers):
    res = ''
    for i in range(len(numbers)):
        if i == pos:
            res += '\033[31m' + str(numbers[i]) + '\033[0m'  # Add ANSI escape sequence for red color
        else:
            res += str(numbers[i])
    res += f' {rule}'
    return res


class NTM:
    def __init__(self, numbers: list[int]):
        self.numbers = numbers
        self.parity_rules = parity_rules
        self.first_rules = first_rules
        self.second_rules = second_rules
        self.sum_rules = sum_rules
        self.firstSecondNumbers = []
        self.results = []
        self.something = []

    def parityCheck(self):
        pos = 1
        rule = 0
        while rule != -1:
            temp_symb, temp_pos, r = self.parity_rules[rule][self.numbers[pos]]
            self.numbers[pos] = temp_symb
            pos += temp_pos
            rule = r
            if pos == len(self.numbers):
                self.numbers.append('b')
            if pos < 0:
                self.numbers.insert(0, 'b')
                pos = 0
            print(smart_print(pos, rule, self.numbers))
            if rule is True or rule is False:
                return rule

    def sumCheck(self, some_numbers):
        numbers = deepcopy(some_numbers)
        good_numbers = deepcopy(some_numbers)
        pos = 1
        rule = 0
        while rule != -1:
            temp_symb, temp_pos, r = sum_rules[rule][numbers[pos]]
            numbers[pos] = temp_symb
            pos += temp_pos
            rule = r
            if pos == len(numbers):
                numbers.append('b')
            if pos < 0:
                numbers.insert(0, 'b')
                pos = 0
            print(smart_print(pos, rule, numbers))
            if rule is True or rule is False:
                break
        return rule, good_numbers

    def firstRule(self, some_numbers):
        numbers = deepcopy(some_numbers)
        pos = 1
        rule = 0
        while rule != -1:
            temp_symb, temp_pos, r = first_rules[rule][numbers[pos]]
            numbers[pos] = temp_symb
            pos += temp_pos
            rule = r
            if pos == len(numbers):
                numbers.append('b')
            if pos < 0:
                numbers.insert(0, 'b')
                pos = 0
            print(smart_print(pos, rule, numbers), ' 1')
            if rule is True or rule is False:
                break
        return rule, numbers

    def secondRule(self, some_numbers):
        numbers = deepcopy(some_numbers)
        pos = 1
        rule = 0
        while rule != -1:
            temp_symb, temp_pos, r = second_rules[rule][numbers[pos]]
            numbers[pos] = temp_symb
            pos += temp_pos
            rule = r
            if pos == len(numbers):
                numbers.append('b')
            if pos < 0:
                numbers.insert(0, 'b')
                pos = 0
            print(smart_print(pos, rule, numbers), ' 2')
            if rule is True or rule is False:
                break
        return rule, numbers

    def firstSecondRule(self, numbers):
        index = 0
        first_check, temp_numbers = self.firstRule(deepcopy(numbers))
        self.something.append(temp_numbers)
        second_check, temp_numbers = self.secondRule(deepcopy(numbers))
        self.something.append(temp_numbers)
        while first_check and second_check:
            first_check, temp_numbers = self.firstRule(deepcopy(self.something[index]))
            self.something.append(temp_numbers)
            second_check, temp_numbers = self.secondRule(deepcopy(self.something[index]))
            self.something.append(temp_numbers)
            index += 1
            if first_check is False:
                print('first false')
            elif first_check is True:
                print('first true')
            if second_check is False:
                print('second false')
            elif second_check is True:
                print('second true')

    def execute(self):
        if not self.parityCheck():
            print("Sum of numbers is odd")
            return
        else:
            print("Sum of numbers is even")
            print("--------------------------------------------------------")
            self.firstSecondRule(self.numbers)
            print("*********************************************************")
            print(self.something)
            for i in self.something:
                temp_check, temp_numbers = self.sumCheck(i)
                if temp_check:
                    self.results.append(temp_numbers)
                else:
                    print('sum false')
            print("RESULTS:")
            for i in self.results:
                print(i)

