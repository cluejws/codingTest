def getResult(n):
    
    dp = [0 for _ in range(n+1)]
    
    # 기저조건1: n=1
    dp[1] = 1
    if n == 1:
        return dp[1]
    
    # 기저조건2: n=2
    dp[2] = 2
    if n == 2:
        return dp[2]
    
    # 계산: dp
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    
    return dp[n]

def solution(n):
    res = getResult(n)
    return res