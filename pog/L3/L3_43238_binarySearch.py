def getResult(n, times):
    
    min_res = 0
    left, right = 0, max(times) * n
    
    # 계산: 이분 탐색
    # 23 29 -> mid:26 -> answer: ??(X)
    # 27 29 -> mid:28 -> answer: 28(O)
    # 27 27 -> mid:27 -> answer: 28(X)
    # 끝
    while left <= right:
        
        mid = (left + right) // 2        
        
        # 1. mid 시간 동안 -> 진행 수
        cnt = 0
        for time in times:
            cnt += (mid // time)
        
        # 2. 진행 수로 판단
        if cnt < n:
            left = mid + 1
        else:
            min_res = mid
            right = mid - 1
        
    return min_res
            
def solution(n, times):
    return getResult(n, times)