import random


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


def inorder_traversal(root, arr):
    if root:
        inorder_traversal(root.left, arr)
        arr.append(root.data)
        inorder_traversal(root.right, arr)


def tree_sort(arr):
    root = None
    for i in range(len(arr)):
        root = insert(root, arr[i])
    arr = []
    inorder_traversal(root, arr)
    return arr


def main():
    arr = [random.randint(1, 50) for i in range(10)]
    print("Array before sort: ", arr)

    arr = tree_sort(arr)
    print("Array after sort: ", arr)


if __name__ == "__main__":
    main()