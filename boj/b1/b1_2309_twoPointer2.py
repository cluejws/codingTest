# 입력
import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]

# 계산0: 난쟁이 아닌 사람 몸무게
sum_res = sum(arr) - 100

# 계산1: 정렬
arr.sort()

# 계산2: twoPointer
left = 0
right = 9 - 1
while left < right:
    if arr[left] + arr[right] == sum_res:
        break
    
    elif arr[left] + arr[right] > sum_res:
        right -= 1
    
    else:
        left += 1

# 출력
for i in range(9):
    if i == left:
        continue
    if i == right:
        continue

    print(arr[i])