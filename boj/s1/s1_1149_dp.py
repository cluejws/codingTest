# 입력
import sys
input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(3)] for _ in range(n)]

# dp 입력 1번 초기화
r,g,b = map(int, input().split())
dp[0][0] = r
dp[0][1] = g
dp[0][2] = b

# dp 입력 n-1번 초기화
for i in range(1, n):
    r,g,b = map(int,input().split())
    
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + r
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + g
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + b

# 출력(n번째의 최솟값)
print(min(dp[-1]))