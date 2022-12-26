import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(1,len(arr)):
        
    # arr[i] < arr[j]  (0 ~ i-1)보다 작음
    # dp[i]  < dp[j]+1 (0 ~ i-1)비교하면서 초기화
    dp[i] = 1
    for j in range(0,i):
        if arr[i] < arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1 
            
print(max(dp))
            
            