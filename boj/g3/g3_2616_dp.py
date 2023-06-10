# 입력
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
k = int(input())

# 계산1: 누적합 계산
prefix_sum = [0 for _ in range(n)]
prefix_sum[0] = arr[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

# 계산2: dp[i][j] = i번째 기관차가 j번째 객차까지 판단 했을 때 최대 값
dp = [[0 for _ in range(n)] for _ in range(3)]

# 2.1: 0번째 기관차
dp[0][(k*1)-1] = prefix_sum[(k*1)-1]
for j in range((k*1) - 1 + 1, n):
    dp[0][j] = max(dp[0][j-1], prefix_sum[j] - prefix_sum[j-k])

# 2.2: 1,2번째 기관차
for i in range(1, 3):
    for j in range((k*(i+1)) - 1, n):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-k] + prefix_sum[j] - prefix_sum[j-k])

# 출력
print(dp[2][n-1])