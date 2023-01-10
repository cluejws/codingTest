n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]


# dp[i] = i를 만들기 위한 최소 동전 개수
dp = [100001 for _ in range(k+1)]

# 계산1: 초기화
dp[0] = 0

# 계산2: dp(bottom up)
# coin을 이용해서 누적
for coin in coins:
    
    for j in range(coin, k+1):
        
        if j - coin >= 0:
            dp[j] = min(dp[j], dp[j - coin] + 1)      

# 출력
if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])