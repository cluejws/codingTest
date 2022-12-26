import sys, math
input = sys.stdin.readline

t = int(input())
for k in range(t):
    price_list = list(map(int,input().split())) # 1일, 1달, 3달, 1년 가격
    month_list = list(map(int,input().split())) # 12개월 이용수
    
    # result[0] -> 현재 달 입력시 1일권 이용
    # result[1] -> 현재 달 입력시 1달권 이용
    # result[2] -> 현재 달 입력시 3달권 이용
    # result[3] -> 현재 달 입력시 1년권 이용
    # dp -> 1달부터 12달까지 누적
    result = [math.inf for _ in range(4)]
    dp = [0 for _ in range(12)]
    dp[0] = min(price_list[0] * month_list[0], price_list[1])
    dp[1] = min(price_list[0] * month_list[1], price_list[1]) + dp[0]
    dp[2] = min(min(price_list[0] * month_list[2], price_list[1]) + dp[1] , price_list[2] + 0)
    
    # 계산
    for i in range(3, len(dp)):
        result[0] = dp[i-1] + price_list[0] * month_list[i] 
        result[1] = dp[i-1] + price_list[1]
        
        if i>=3: 
            result[2] = dp[i-3] + price_list[2]
        
        if i==11: 
            result[3] = price_list[3]
        
        dp[i] = min(result)
    
    print("#"+str(k+1), end=" ")
    print(dp[-1])    
    
    