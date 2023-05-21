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
for i in range(n):
    for j in range(k+1):

        # 1. (최대 누적) 도보
        # -> 만약 if 만족하면 (dp[i][j] = 0 일때)
        if j >= time[i][0]:
            dp[i][j] = max(dp[i][j], dp[i-1][j - time[i][0]] + price[i][0])
        
        # 2. (최대 누적) 자전거
        # -> 만약 if 만족하면 (dp[i][j] = 0 일때, 도보 일때)
        if j >= time[i][1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j - time[i][1]] + price[i][1])
        
        # 3. 불가능
        if j < time[i][0] and j < time[i][1]:
            dp[i][j] = dp[i-1][j]

# 출력
print(dp[n-1][k])
    