import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

dp = [0 for _ in range(n)]
dp[0] = 1
for i in range(1,n):
    
    dp[i] = 1
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(dp))