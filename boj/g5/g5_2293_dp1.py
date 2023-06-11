# 입력
import sys, math
input= sys.stdin.readline

n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]

# dp[i] = i를 만드는 경우의 수(동전의 가치는 다름)
dp = [0 for _ in range(k+1)]

# 계산1: 초기화
dp[0] = 1

# 계산2: dp
for coin in coins:
    for j in range(coin, k+1):
        if j - coin >= 0:
            dp[j] += dp[j - coin]

# 출력
print(dp[k])