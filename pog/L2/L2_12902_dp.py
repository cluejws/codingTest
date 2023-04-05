def getResult(n):
    
    dp = [0 for _ in range(n+1)]
    
    # 기저조건1: 홀수
    if n % 2 == 1:
        return dp[n]
    
    # 기저조건2: n == 2
    dp[2] = 3
    if n == 2:
        return dp[2]
    
    # 계산: dp  
    for i in range(4, n+1, 2):
        
        # 계산1: 2*1로 3개의 경우
        dp[i] = dp[i-2] * 3
        
        # 계산2: 2*n로 특이한 문양의 경우
        for j in range(i-4, 0, -2):
            dp[i] += dp[j] * 2
            
        # 계산3: 특이한 문양의 경우
        dp[i] += 2
        
        # 계산4: 효율성
        dp[i] = dp[i] % 1000000007
    
    return dp[n] 
    
    
def solution(n):
    res = getResult(n)
    return res