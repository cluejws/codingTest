# 입력
import sys, heapq, math
input = sys.stdin.readline
v,e = map(int,input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
heap = []
dist = [math.inf for _ in range(v+1)]
for _ in range(e):
    
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

# 계산1: 다익스트라 초기화
dist[k] = 0
heapq.heappush(heap, (dist[k], k))

# 계산2: 다익스트라
while len(heap) != 0:
    
    min_dist, min_index = heapq.heappop(heap)
    
    if dist[min_index] < min_dist:
        continue
    
    for target_index, target_dist in graph[min_index]:
        next_dist = min_dist + target_dist
        
        if dist[target_index] > next_dist:
            dist[target_index] = next_dist
            heapq.heappush(heap, (next_dist, target_index))
        
# 출력
for i in range(1, v+1):
    if dist[i] == math.inf:
        print('INF')
    else:
        print(dist[i])