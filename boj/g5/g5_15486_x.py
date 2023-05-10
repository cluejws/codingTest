# 입력
import sys 
input = sys.stdin.readline

n = int(input())

# 계산: dp
# dp[i] = i일까지 최대 이익
# dp[일 할 수 없는 날짜] = 0
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    time, point = map(int,input().split())

    # 1: 1일 -> 최대값 할당
    if i + time - 1 <= n:
        dp[i + time - 1] = max(dp[i + time - 1], point)

    # 2: 1일 이후 (1일 ~ i-1일) -> 최대값 할당
    for j in range(1, i):
        if i + time - 1 <= n:
            dp[i + time - 1] = max(dp[i + time - 1], dp[j] + point)
    print(dp)
# 출력
print(max(dp))