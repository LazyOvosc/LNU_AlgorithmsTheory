import random


def list_create():
    list_1 = [random.randint(0, 10) for _ in range(30)]
    list_2 = [random.randint(0, 10) for _ in range(30)]
    list_3 = [random.randint(0, 10) for _ in range(30)]
    list_1.sort()
    list_2.sort()
    list_3.sort()
    return list_1, list_2, list_3


def common_check(arr1, arr2, arr3):
    common_numbers = set(arr1) & set(arr2) & set(arr3)
    if len(common_numbers) > 0:
        print(common_numbers)
        return True
    return False


def find_smallest_common_number(arr1, arr2, arr3):
    smallest_number = 10**10
    i = j = k = 0

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        min_val = min(arr1[i], arr2[j], arr3[k])
        if min_val in arr1 and min_val in arr2 and min_val in arr3:
            smallest_number = min(smallest_number, min_val)
        if min_val == arr1[i]:
            i += 1
        elif min_val == arr2[j]:
            j += 1
        else:
            k += 1

    return smallest_number


list1, list2, list3 = list_create()

while not common_check(list1, list2, list3):
    list1, list2, list3 = list_create()

min = find_smallest_common_number(list1, list2, list3)
print(min)



