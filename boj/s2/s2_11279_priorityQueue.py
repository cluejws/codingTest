import heapq, sys
input = sys.stdin.readline

n = int(input())
max_heap = []
for _ in range(n):
    
    line = int(input())
    if line > 0:
        heapq.heappush(max_heap, -line)
        
    elif line == 0:
        if len(max_heap) == 0:
            print(0)
            continue
        
        print(-heapq.heappop(max_heap))