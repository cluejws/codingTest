def solution(N, number):
    # 계산1: dp 초기화
    # dp[i] = (i개 만큼 N을 사용)한 후보들
    dp = [set() for i in range(8+1)]
    for i in range(1, 8+1):
        dp[i].add(int(str(N)*(i)))
    
    # 계산2: dp
    # 순회
    for i in range(1, 8+1):        
        # 2-1: j 기준 순회(j < i)
        for j in range(i):
            
            # dp[i] = (dp[j], dp[i-j])
            # 예시: dp[3] = (dp[1], dp[2]) (dp[2], dp[1])
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
        
        # 2-2: 기저조건
        if number in dp[i]:
            return i
        
    return -1