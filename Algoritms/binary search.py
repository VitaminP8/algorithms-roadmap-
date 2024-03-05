def binary_search(arr: list, x: int):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return False


n, k = map(int, input().split())
arr1 = list(map(int, input().split()))[:n]
arr2 = list(map(int, input().split()))[:k]
arr1.sort()

for i in arr2:
    if binary_search(arr1, i):
        print('YES')
    else:
        print('NO')
