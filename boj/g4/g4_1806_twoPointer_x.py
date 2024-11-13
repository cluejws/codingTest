# 입력
import sys, math
input = sys.stdin.readline

n, s = map(int,input().split())
arr = list(map(int,input().split()))

# 계산: two Pointer
sum_res = 0
j = 0
min_res = math.inf

sum_res = arr[0]
for i in range(n):
    
    # 계산1: 합이 s이상의 최대 구간 구하기
    while j + 1 < n and sum_res < s:
        sum_res += arr[j+1]
        j += 1     
    
    # 계산2: 최대 구간 구했는데 목표값 안됨 break
    if sum_res < s:
        break        

    # 계산2: 최소길이 할당
    min_res = min(min_res, j-i+1)
    
    # 계산3: 다음 구간 위한 변화
    sum_res -= arr[i]
    
# 출력
if min_res == math.inf:
    print(0)
else:
    print(min_res)