def TwoPoint (arr: list, x: int):
    left_pointer = 0
    right_pointer = len(arr) - 1
    sum = 0
    while left_pointer != right_pointer:
        sum = arr[left_pointer] + arr[right_pointer]
        if sum < x:
            left_pointer += 1
        elif sum > x:
            right_pointer -= 1
        else:
            break
    if sum == x:
        ans = [left_pointer, right_pointer]
        print(ans)
    else:
        print(-1)



n = int(input())
arr = list(map(int, input().split()))
arr.sort()
target = int(input())
TwoPoint(arr, target)


