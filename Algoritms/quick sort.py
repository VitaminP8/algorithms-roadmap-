def prefix_sum (arr: list):
    max_index = len(arr)
    prefix_sum_array = [0] * max_index
    prefix_sum_array[0] = arr[0]

    for i in range(1, max_index):
        prefix_sum_array[i] = prefix_sum_array[i-1] + arr[i]

    return prefix_sum_array


n = int(input())
arr = list(map(int, input().split()))
pref_arr = prefix_sum(arr)

k = int(input())
ans = list()
for i in range(k):
    left, right = map(int, input().split())
    left_index = left - 1
    right_index = right - 1
    if left_index == 0:
        ans.append(pref_arr[right_index])
    elif left_index == right_index:
        ans.append(arr[right_index])
    else:
        ans.append(pref_arr[right_index] - pref_arr[left_index-1])

# print(arr)
# print(pref_arr)
print(ans)

