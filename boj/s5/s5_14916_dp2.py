# 입력
import sys, math
input = sys.stdin.readline

n = int(input())
coins = [2, 5]

# dp[i] = i를 만드는 최소의 동전 개수(동전의 가치는 다름)
dp = [math.inf for _ in range(n+1)]

# 계산1: dp 초기화
dp[0] = 0

# 계산2: dp
for i in range(1, n+1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i - coin] + 1)

# 출력
if dp[n] == math.inf:
    print(-1)
else:
    print(dp[n])