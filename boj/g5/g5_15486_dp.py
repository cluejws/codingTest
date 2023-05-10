# 입력
import sys 
input = sys.stdin.readline

n = int(input())

# 계산: dp
# dp[i] = i일까지 최대 이익
# dp[일 할 수 없는 날짜] = dp[일 할 수 없는 날짜 - 1]
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    time, point = map(int,input().split())

    # 1: (i일 전 -> 일하지 않은 날짜)와 (i일 전 -> 일 한 날짜) 최대값 구하기
    # 일 할 수 없는 날짜 반영  
    dp[i] = max(dp[i-1], dp[i])

    # 2: (i일 -> 일하지 않는 날짜)와 (i일 -> 일 하는 날짜) 최대값 구하기
    if i + time - 1 <= n:
        dp[i + time - 1] = max(dp[i + time - 1], dp[i-1] + point)

    print(dp)

# 출력
print(dp[-1])