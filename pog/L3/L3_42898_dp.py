def solution(m, n, puddles):
    
    # 계산1: 그래프 생성
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for puddle in puddles:
        x, y = puddle
        dp[y-1][x-1] = -1
    
    # 계산2: dp
    # 1. 세로 초기화
    breakId = -1
    for j in range(1, m):
        if dp[0][j] == -1:
            breakId = j
            break
        
        dp[0][j] = 1
    
    if breakId != -1:
        for j in range(breakId, m):
            dp[0][j] = -1
    
    # 2. 가로 초기화
    breakId = -1
    for i in range(1, n):
        if dp[i][0] == -1:
            breakId = i
            break
        
        dp[i][0] = 1
        
    if breakId != -1:
        for i in range(breakId, n):
            dp[i][0] = -1
    
    # 3. dp
    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] == -1:
                continue
                
            if dp[i-1][j] == -1 and dp[i][j-1] == -1:
                dp[i][j] = -1
            elif dp[i-1][j] == -1:
                dp[i][j] = (dp[i][j-1]) % 1000000007
            elif dp[i][j-1] == -1:
                dp[i][j] = (dp[i-1][j]) % 1000000007
            else:
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000007
    
    # 계산3: return 없을 경우 / 있을 경우
    if dp[n-1][m-1] == -1:
        return 0
    
    return dp[n-1][m-1]