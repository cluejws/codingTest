def getLevel(diffs, times, limit, dp):
    # 초기화
    n = len(diffs)
    min_level = 100000
    
    # 매개변수 탐색
    left, right = 1, 100000
    while left <= right:
        # 1.
        mid = (left + right) // 2
        
        # 2.
        time = 0
        for i in range(n):
            if diffs[i] <= mid:
                time += times[i]
            else:
                time += ((diffs[i] - mid) * dp[i]) + times[i]
        
        # 3.
        if time > limit:
            left = mid + 1
        else:
            min_level = min(min_level, mid)
            right = mid - 1
            
    return min_level

def solution(diffs, times, limit):
    # 초기화
    n = len(diffs)
    
    # 계산1: dp
    # dp[i] = 틀리는 시간
    dp = [0 for _ in range(n)]
    dp[0] = 0
    for i in range(1, n):
        dp[i] = times[i] + times[i-1]
    
    # 계산2: 매개변수 탐색
    min_level = getLevel(diffs, times, limit, dp)
    return min_level