# 입력
import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]

# 기저조건1
dp[1] = 1
if n == 1:
    print(dp[1])
    quit()

# 기저조건2
dp[2] = 2
if n == 2:
    print(dp[2])
    quit()

# 계산: dp
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

# 출력
print(dp[n])