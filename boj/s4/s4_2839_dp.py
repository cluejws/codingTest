# 입력
import sys
input = sys.stdin.readline

n = int(input())

# 계산: dp
dp = [-1 for _ in range(n+1)]

# 계산1: 5 미만
dp[3] = 1
if n <= 4:
    print(dp[n])
    quit()
    
# 계산2: 5 이상
dp[5] = 1
for i in range(6, n+1):

    if dp[i-3] == -1 and dp[i-5] == -1:
        continue
    
    elif dp[i-3] == -1 and dp[i-5] != -1:
        dp[i] = dp[i-5] + 1
    
    elif dp[i-3] != -1 and dp[i-5] == -1:
        dp[i] = dp[i-3] + 1
    
    else:
        dp[i] = min(dp[i-3], dp[i-5]) + 1

# 출력
print(dp[n])