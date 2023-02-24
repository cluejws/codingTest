def getResult(operations):
    
    max_heap = []
    min_heap = []
    visited = [False for _ in range(1000000+1)]
    
    # 계산1: 명령문 처리
    for i in range(len(operations)):
        line, value = operations[i].split()
        if line == 'I':    
            heapq.heappush(max_heap, (-int(value), i))
            heapq.heappush(min_heap, (int(value), i))
            visited[i] = True
            
        elif line == 'D' and value == '1':
            
            # (1) 이전 삭제된 것 처리
            while len(max_heap) > 0 and visited[max_heap[0][1]] == False:
                data, index = heapq.heappop(max_heap)
                data = -data
                
            # (2) 현재 삭제
            if len(max_heap) > 0:
                data, index = heapq.heappop(max_heap)
                visited[index] = False
        
        elif line == 'D' and value == '-1':    
            
            # (1) 이전 삭제된 것 처리
            while len(min_heap) > 0 and visited[min_heap[0][1]] == False:
                data, index = heapq.heappop(min_heap)
            
            # (2) 현재 삭제
            if len(min_heap) > 0:
                data, index = heapq.heappop(min_heap)
                visited[index] = False
                
    # 계산2: 이전 삭제된 것 처리
    while len(max_heap) > 0 and visited[max_heap[0][1]] == False:
        data, index = heapq.heappop(max_heap)
        data = -data
    while len(min_heap) > 0 and visited[min_heap[0][1]] == False:
        data, index = heapq.heappop(min_heap)
        
    # 계산3: return
    if len(max_heap) == 0 or len(min_heap) == 0:
        return [0,0]
    else:
        return [-max_heap[0][0], min_heap[0][0]]
                

import heapq

def solution(operations):
    
    res = getResult(operations)
    return res