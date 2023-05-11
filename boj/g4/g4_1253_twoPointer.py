def getResult(temp_arr, target):

    left = 0
    right = len(temp_arr) - 1

    while left < right:
        
        sum_res = temp_arr[left] + temp_arr[right]

        if sum_res > target:
            right -= 1
        elif sum_res < target:
            left += 1
        else:
            return True
    
    return False
    
# 입력
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

# 계산1: 정렬
arr.sort()

# 계산2: 매 지점 마다 twoPointer
cnt = 0
for i in range(n):
    if getResult(arr[:i] + arr[i+1:], arr[i]):
        cnt += 1

# 출력
print(cnt)
