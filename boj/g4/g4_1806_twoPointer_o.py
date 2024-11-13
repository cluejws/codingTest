# 입력
import sys, math
input = sys.stdin.readline

n, s = map(int,input().split())
arr = list(map(int,input().split()))

# 계산: 투포인터
min_res = math.inf
sum_res = 0
j = 0

sum_res = arr[0]
for i in range(n):
    
    # 1. j를 s 이상 될 때까지, 초과해서(>=s) 이동
    while j + 1 < n and sum_res < s:
        sum_res += arr[j + 1]
        j += 1     
    
    # 2. 기저조건
    if sum_res < s:
        break        

    # 3. 최소 길이 할당
    min_res = min(min_res, j-i+1)
    
    # 4. 다음 준비
    sum_res -= arr[i]
    
# 출력
if min_res == math.inf:
    print(0)
else:
    print(min_res)