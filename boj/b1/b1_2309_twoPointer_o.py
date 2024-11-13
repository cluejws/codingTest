def print_res(left, right, arr):
    for i in range(n):
        if (left == i) or (right == i):
            continue

        print(arr[i])

# 입력
import sys
input = sys.stdin.readline

n = 9
arr = [int(input()) for _ in range(n)]

# 계산1: 정렬
arr.sort()

# 계산2: 투포인터
over_weight = sum(arr) - 100
left = 0
right = n - 1

while left < right:
    # 1.
    if arr[left] + arr[right] == over_weight:
        print_res(left, right, arr)
        quit()

    # 2.
    if arr[left] + arr[right] > over_weight:
        right -= 1
    elif arr[left] + arr[right] < over_weight:
        left += 1