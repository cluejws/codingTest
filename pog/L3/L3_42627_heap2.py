from collections import deque
import heapq
        
def solution(jobs):
    # 계산1: 정렬(도착시간, 걸리는 시간)
    jobs.sort()
    jobs = deque(jobs)
    
    # 계산2: 현재 가능 판단 / 현재 가능 이동
    n = len(jobs)
    cnt = 0
    
    time = 0
    sum_res = 0
    heap = []
    while cnt < n:
        # 1. (현재 가능) 시 추가
        while len(jobs) > 0 and time >= jobs[0][0]:
            # 1-1
            arrive_time, len_res = jobs.popleft()
            heapq.heappush(heap, (len_res, arrive_time))
            
        # 2. (현재 가능 없음) 시 추가
        if len(jobs) > 0 and len(heap) == 0:
            # 2-1
            arrive_time, len_res = jobs.popleft()
            heapq.heappush(heap, (len_res, arrive_time))
            
            # 2-2
            time = arrive_time
            
        # 3. 현재 가능 이동
        # 3-1
        len_res, arrive_time = heapq.heappop(heap)

        # 3-2: 
        sum_res += (time - arrive_time) + (len_res)
        time += (len_res)
        cnt += 1
        
    return sum_res // n