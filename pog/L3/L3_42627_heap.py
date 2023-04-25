import heapq

def getResult(jobs):
    
    n = len(jobs)
    cnt = 0
    
    # 계산: 최대한 우선순위 큐 넣고 판단
    # heap(가장 작은 시간, 가장 작은 시작점)
    # sum_res(걸린 시간)
    # pos(현재 시작점)
    heap = []
    sum_res = 0
    pos = 0
    while cnt < n:
        
        # 1. 우선순위 큐 생성(현재 실행할 수 있는 작업)
        while len(jobs) > 0 and pos >= jobs[0][0]:
            job_pos, time = jobs.pop(0)
            heapq.heappush(heap, (time, job_pos))
           
        # 2. 우선순위 큐 없을 경우(현재 실행 할 수 없을 경우 / 시작점 이동)
        if len(jobs) > 0 and len(heap) == 0:
            job_pos, time = jobs.pop(0)
            heapq.heappush(heap, (time, job_pos))
            pos = job_pos
    
        # 3. (가장 작은 시간, 가장 작은 시작점) 실행
        time, job_pos = heapq.heappop(heap)
        sum_res += (pos - job_pos) + (time)
        pos += time
        cnt += 1
    
    return sum_res // n

def solution(jobs):
    
    # 1. 정렬(시작점, 시간)
    jobs.sort(key=lambda x:(x[0], x[1]))
    
    # 2. 최소 평균 작업 시간
    res = getResult(jobs)
    return res