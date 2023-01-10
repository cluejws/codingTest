# 입력
k = int(input())

# dp[i][0] -> A개수
# dp[i][1] -> B개수
dp = [[-1,-1] for _ in range(k+1)]

# 계산1: 초기화
dp[1] = [0, 1]

# 계산2: dp: bottom up
for i in range(2, k+1):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = dp[i-1][0] + dp[i-1][1]

# 출력
print(dp[k][0], dp[k][1])    