import random


def digit_sort(arr):
    max_digits = len(str(max(arr)))
    for i in range(max_digits):
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = num // 10**i % 10
            buckets[digit].append(num)
        arr = [num for bucket in buckets for num in bucket]
    return arr


def main():
    arr = [random.randint(100, 1000) for i in range(10)]
    print("Array before sort: ", arr)
    sorted_arr = digit_sort(arr)
    print("Array after sort: ", sorted_arr)


if __name__ == "__main__":
    main()