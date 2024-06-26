# 입력
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]

# 계산1: 초기화
# dp[i] = i를 만드는 경우의 수
dp = [0 for _ in range(k+1)]
dp[0] = 1

# 계산2: dp
# coin=2 누적
# (coin=2, i=3, dp[3-2])[1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1]
# (coin=2, i=4, dp[4-2])[1, 1, 2, 2, 3, 1, 1, 1, 1, 1, 1]
# (coin=2, i=5, dp[5-2])[1, 1, 2, 2, 3, 3, 1, 1, 1, 1, 1]
for coin in coins:
    for i in range(coin, k+1):
        if (i - coin) >= 0:
            dp[i] += dp[i - coin]

# 출력
print(dp[k])