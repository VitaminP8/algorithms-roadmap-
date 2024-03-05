def heapify (arr, n , i):
    largest = i
    left_child = i*2 + 1
    right_child = i*2 + 2

    if left_child < n and arr[largest] < arr[left_child]:
        largest = left_child

    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def HeapSort(arr):
    n = len(arr)

    # Построение max-heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)



arr = list(map(int, input().split()))
HeapSort(arr)
print(arr)
