# 입력
import sys, math
input = sys.stdin.readline

n, k = map(int,input().split())
dolls = list(map(int,input().split()))

# 계산1: twoPointer
min_res = math.inf
cnt = 0
j = 0

# 초기화
if dolls[j] == 1:
    cnt += 1
for i in range(n):

    # 1. j를 k개 만족 할때까지 이동
    while j + 1 < n and cnt < k:
        if dolls[j+1] == 1:
            cnt += 1
        j += 1

    # 2. j를 k 될때까지 x
    if cnt < k:
        break
    
    # 3. 최소 길이 할당
    min_res = min(min_res, j - i + 1)

    # 4. 다음 준비
    if dolls[i] == 1:
        cnt -= 1 

# 출력
if min_res == math.inf:
    print(-1)
else:
    print(min_res)