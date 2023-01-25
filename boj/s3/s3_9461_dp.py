import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    n = int(input())
    if n == 1:
        print(1)
        continue
    elif n == 2:
        print(1)
        continue
    elif n == 3:
        print(1)
        continue
    elif n == 4:
        print(2)
        continue
    elif n == 5:
        print(2)
        continue
    else:    
        dp = [-1 for i in range(n+1)]
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2
        dp[5] = 2    
        
        for i in range(6, n+1):
            dp[i] = dp[i-1] + dp[i-5]
        
        print(dp[n])