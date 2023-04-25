import heapq

def check(heap, k):
    
    for h in heap:
        if h < k:
            return False
        
    return True

def getResult(scoville, k):
    
    # 계산1: 최소 힙 생성
    heap = []
    for sc in scoville:
        heapq.heappush(heap, sc)
        
    # 계산2: 조건 판단 -> 섞기
    cnt = 0
    while len(heap) >= 2:
        
        # 1. 판단
        if check(heap, k):
            return cnt
        
        # 2. 섞기
        sc1 = heapq.heappop(heap)
        sc2 = heapq.heappop(heap)
        new_sc = sc1 + (sc2 * 2)
        
        heapq.heappush(heap, new_sc)
        cnt += 1
        
    # 계산3: 1개 일때 조건 판단
    if check(heap, k):
        return cnt
    
    return -1
    
def solution(scoville, K):
    res = getResult(scoville, K)
    return res