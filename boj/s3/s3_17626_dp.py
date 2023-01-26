# 계산
import sys, math
input = sys.stdin.readline

n = int(input())

# 계산: dp
dp = [0 for _ in range(n+1)]
dp[1] = 1
for i in range(2, n+1):
    
    # 계산1: 최소 길이 얻기
    min_value = math.inf
    for j in range(1, int(i ** (1/2)) + 1):
        min_value = min(min_value, dp[i - j ** 2])
        
    # 계산2: 최소 길이에서 + 1
    dp[i] = min_value + 1

# 출력
print(dp[n])