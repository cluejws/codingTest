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
j = n - 1

if arr[0] + arr[n-1] == over_weight:
    print_res(0, n-1, arr)
    quit()
for i in range(n):

    # 1. j가 over_weight 이하가 될 때까지, 초과해서(<= over_weight) 이동
    while j - 1 >= 0 and arr[i] + arr[j] > over_weight:
        j -= 1

    # 2. 기저 조건
    if i >= j:
        break

    # 3. 할당
    if arr[i] + arr[j] == over_weight:
        print_res(i, j, arr)
        quit()