# 입력
import sys, math
input= sys.stdin.readline

n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [math.inf for _ in range(k+1)]

# 계산1: 초기화
dp[0] = 0

# 계산2: dp
for coin in coins:
    for j in range(coin, k+1):
        if j >= coin:
            dp[j] = min(dp[j], dp[j - coin] + 1)      

# 출력
if dp[k] == math.inf:
    print(-1)
else:
    print(dp[k])