import random


def list_create():
    arr = [[random.randint(0, 20) for _ in range(5)] for _ in range(3)]
    return arr


def list_check():
    for i in range(len(l)):
        l[i].sort()
    first_check = True
    for i in range(len(l[0])):
        for j in range(len(l)-1):
            if l[j][i] > l[j+1][i]:
                first_check = False
                break
    if first_check:
        return True
    return False


def search_2d_array(arr, to_find):
    m, n = len(arr), len(arr[0])
    i, j = 0, n-1
    while i < m and j >= 0:
        if arr[i][j] == to_find:
            return True
        elif arr[i][j] > to_find:
            j -= 1
        else:
            i += 1
    return False


def list_print(arr):
    for row in arr:
        print(row)


l = list_create()

while not list_check():
    l = list_create()

list_print(l)

number_to_find = int(input("Enter number to find: "))

if search_2d_array(l, number_to_find):
    print("Number found")
else:
    print("Number not found")

