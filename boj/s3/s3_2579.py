import sys
input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(input())
    

if n >= 3:
    dp = [0 for _ in range(n)]
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[1]+arr[2], arr[0] + arr[2])

    for i in range(3,n):
        dp[i] = max(dp[i-3]+ arr[i-1]+ arr[i], dp[i-2]+ arr[i])

    print(dp[n-1])
else:
    print(sum(arr))
