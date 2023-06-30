import random

list_1 = []
list_2 = []

for i in range(20):
    list_1.append(random.randint(0, 10))
for i in range(5):
    list_2.append(random.randint(0, 10))

list_1.sort()
list_2.sort()


def can_delete_to_get_b(list1, list2):
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            return False

    return j == len(list2)


print(list_1)
print(list_2)

if can_delete_to_get_b(list_1, list_2):
    print('Yes')
else:
    print('No')
