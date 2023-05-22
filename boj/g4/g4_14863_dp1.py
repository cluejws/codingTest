# 입력
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
time = []
price = []
for _ in range(n):
    t1, p1, t2, p2 = map(int,input().split())
    time.append((t1, t2))
    price.append((p1, p2))

# 계산: dp
# dp[i][j] = i번째까지 고려했을때 j시간일때 최대 가치
dp = [[0 for _ in range(k+1)] for _ in range(n)]

# 계산1: dp 초기화
for j in range(k+1):

    if j >= time[0][0]:
        dp[0][j] = max(dp[0][j], price[0][0])
    
    if j >= time[0][1]:
        dp[0][j] = max(dp[0][j], price[0][1])

# 계산2: dp 계산
for i in range(1, n):
    for j in range(k+1):

        # 1. 도보
        # -> 만약 if 만족하면 (도보 일때)
        if j >= time[i][0] and dp[i-1][j - time[i][0]] > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j - time[i][0]] + price[i][0])
        
        # 2. 자전거
        # -> 만약 if 만족하면 (도보 일때, 자전거 일때)
        if j >= time[i][1] and dp[i-1][j - time[i][1]] > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j - time[i][1]] + price[i][1])

# 출력
print(max(dp[n-1]))