# 입력
import sys
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n)]
dp = [[] for _ in range(n)] 
for i in range(n):
    arr = list(map(int,input().split())) 
    
    graph[i] = arr
    dp[i] = [0 for _ in range(len(arr))] 

# 계산1: dp 초기화
dp[0][0] = graph[0][0]
if n == 1:
    print(max(dp[-1]))
    quit()

dp[1][0] = dp[0][0] + graph[1][0]
dp[1][1] = dp[0][0] + graph[1][1]
if n == 2:
    print(max(dp[-1]))
    quit()

# 계산2: dp 계산
for i in range(2, n):

    dp[i][0] = dp[i-1][0] + graph[i][0]

    for j in range(1, len(graph[i])-1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + graph[i][j]

    dp[i][-1] = dp[i-1][-1] + graph[i][-1]

# 출력
print(max(dp[-1]))