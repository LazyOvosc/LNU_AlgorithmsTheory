import random


n = 20
m = 50
list_n = []
list_m = []
final_list = []

for i in range(n):
    list_n.append(random.randint(0, 100))
for i in range(m):
    list_m.append(random.randint(0, 100))

list_n.sort()
list_m.sort()


def merge_arrays(list1, list2):
    m = len(list1)
    n = len(list2)
    final = [0] * (m + n)

    i = j = k = 0
    while i < m and j < n:
        if list1[i] <= list2[j]:
            final[k] = list1[i]
            i += 1
        else:
            final[k] = list2[j]
            j += 1
        k += 1

    while i < m:
        final[k] = list1[i]
        i += 1
        k += 1

    while j < n:
        final[k] = list2[j]
        j += 1
        k += 1

    return final


final_list = merge_arrays(list_n, list_m)

print(list_n)
print(list_m)
print(final_list)
