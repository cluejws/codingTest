# 입력
import sys, math
input = sys.stdin.readline

n = int(input())
coins = [2, 5]
dp = [math.inf for _ in range(n+1)]

# 계산1: dp 초기화
dp[0] = 0

# 계산2: dp
for coin in coins:
    
    for j in range(coin, n+1):
        
        if j - coin >= 0:
            dp[j] = min(dp[j], dp[j - coin] + 1) 

# 출력
if dp[n] == math.inf:
    print(-1)
else:
    print(dp[n])