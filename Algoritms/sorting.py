def quicksort (arr: list):
    if len(arr) <= 1:
        return arr

    point = arr[len(arr) // 2]
    left = [x for x in arr if x < point]
    middle = [x for x in arr if x == point]
    right = [x for x in arr if x > point]

    ans = quicksort(left) + middle + quicksort(right)
    return ans


arr = list(map(int, input().split()))
quick_sorted_arr = quicksort(arr)
print(quick_sorted_arr)



