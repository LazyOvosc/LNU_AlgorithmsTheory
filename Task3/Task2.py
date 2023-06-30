import random


def counting_sort(arr, k):
    count = [0] * (k+1)
    for i in arr:
        count[i] += 1
    for i in range(1, k+1):
        count[i] += count[i-1]
    result = [0] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        result[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    return result


def main():
    arr = [random.randint(1, 50) for i in range(10)]
    print("Array before sort: ", arr)
    k = max(arr) + 1
    sorted_arr = counting_sort(arr, k)
    print("Array after sort: ", sorted_arr)


if __name__ == '__main__':
    main()
