# 입력
import sys
input = sys.stdin.readline

n = int(input())

# 계산
if n == 1:
    print(1 % 10007)
    quit()
elif n == 2:
    print(3 % 10007)
    quit()
else:
    
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    dp[2] = 3

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] * 2

    print(dp[n] % 10007)