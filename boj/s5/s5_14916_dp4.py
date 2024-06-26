# 입력
import sys, math
input = sys.stdin.readline

k = int(input())
coins = [2, 5]

# 계산1: 초기화 
# dp[i] = i를 거슬러 주기 위한 최소 동전 수
dp = [math.inf for _ in range(k+1)]
dp[0] = 0

# 계산2: dp
for coin in coins:
    for i in range(1, k+1):
        if (i - coin) >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)

# 출력
if dp[k] == math.inf:
    print(-1)
else:
    print(dp[k])