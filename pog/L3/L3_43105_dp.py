def getDP(triangle):
    
    dp = [item[:] for item in triangle]
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            dp[i][j] = 0

    return dp
            
def solution(triangle):
    
    # 계산0: dp 초기화
    dp = getDP(triangle)
    
    # 계산: dp(기저조건 1)
    dp[0][0] = triangle[0][0]
    if len(dp) == 1:
        return dp[0][0]
    
    # 계산: dp(기저조건 2)
    dp[1][0] = triangle[1][0] + dp[0][0]
    dp[1][1] = triangle[1][1] + dp[0][0]
    if len(dp) == 2:
        return max(dp[1][0], dp[1][1])
    
    # 계산: dp
    for i in range(2, len(dp)):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
                continue
            
            elif j == (len(dp[i]) - 1):
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                continue
            
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    return max(dp[-1])