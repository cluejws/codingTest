# 입력
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

# 계산: dp[i][j] = i번째 까지 고려했을 때 j를 만들 수 있는 경우의 수
dp = [[0 for _ in range(21)] for _ in range(n-1)]

# 계산1: 초기화
dp[0][arr[0]] = 1

# 계산2: dp
for i in range(1, n-1):
    for j in range(21):
        if dp[i-1][j] > 0:
            if 0<= j + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i-1][j]
            
            if 0<= j - arr[i] <= 20:
                dp[i][j - arr[i]] += dp[i-1][j]
            
# 출력
print(dp[n-2][arr[n-1]])