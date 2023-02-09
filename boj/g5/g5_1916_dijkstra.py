def dijkstra(start, end):
    
    heap = []
    heapq.heappush(heap, (0, start))
    dist[start] = 0
    
    while len(heap) != 0:
        
        min_dist, min_index = heapq.heappop(heap)
        
        if dist[min_index] < min_dist:
            continue
        
        for target_index, target_dist in graph[min_index]:
            
            new_dist = dist[min_index] + target_dist
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist
                heapq.heappush(heap, (new_dist, target_index))
    
    return dist[end]
    
# 입력
import sys, math, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dist = [math.inf for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
# 계산: 시작 -> 도착 (다익스트라)
start, end = map(int,input().split())
min_dist = dijkstra(start, end)

# 출력
print(min_dist)