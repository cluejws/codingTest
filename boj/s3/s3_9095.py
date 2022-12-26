def getResult(n):
    
    dp = [0 for _ in range(n+1)]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
    return dp[n]

import sys
input = sys.stdin.readline

t = int(input())
print_t = []
for _ in range(t):
    n = int(input())
    print_t.append(getResult(n))
    
for pt in print_t:
    print(pt)