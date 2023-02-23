# 입력
import sys
input = sys.stdin.readline

h,w = map(int,input().split())
arr = list(map(int,input().split()))

# 계산: 빗물 계산
sum_res = 0
for i in range(len(arr)):
    
    # (1): 현재부터 왼쪽까지 최대
    max_left = max(arr[:i+1])
    
    # (2): 현재부터 오른쪽까지 최대
    max_right = max(arr[i:])
    
    # (3): (1),(2) 최소값
    min_LeftRight = min(max_left, max_right)
    
    # (4): 빗물 계산
    sum_res += (min_LeftRight - arr[i])    

# 출력
print(sum_res)