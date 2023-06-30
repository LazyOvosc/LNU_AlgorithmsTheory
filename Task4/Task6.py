import random
import re
from colorama import Fore


def generate_random_string():
    length = random.randint(10, 100)

    letters = ['a', 'b', 'c']
    rand_string = ''.join(random.choices(letters, k=length))

    first_a = rand_string.find('a')
    rand_string_a = rand_string[:first_a + 1] + rand_string[first_a + 1:].replace('a', '')

    return rand_string, rand_string_a


def checker():
    for i in range(100):
        l, l_a = generate_random_string()
        if removal(l) == l_a:
            print(Fore.GREEN + 'True' + Fore.RESET)
        else:
            print(l)
            print(removal(l))
            print(l_a)
            print(Fore.RED + 'False' + Fore.RESET)


def removal(a: str):
    while True:
        if 'aa' in a:
            a = a.replace('aa', 'a', 1)
        elif 'a' in a:
            a = a.replace('a', 'A', 1)
        elif 'AA' in a:
            a = a.replace('AA', 'A', 1)
        elif re.search(r'A([b,c])', a):
            a = re.sub(r'A([b,c])', r'|\1A', a, count=1)
        elif re.search(r'([b,c])A', a):
            a = re.sub(r'([b,c])A', r'\1|A', a, count=1)
        elif 'A' in a:
            a = a.replace('A', '', 1)
        elif re.search(r'\|([b,c])\|', a):
            a = re.sub(r'\|([b,c])\|', r'\1|', a[::-1], count=1)[::-1]
        elif '|' in a:
            a = a.replace('|', 'a', 1)
            break
        else:
            break
    return a


print(removal('aaa'))
checker()
