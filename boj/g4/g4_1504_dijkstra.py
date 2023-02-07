def dijkstra(start):
    dist = [math.inf for _ in range(n+1)]
    heap = []
    
    heapq.heappush(heap, (0, start))
    dist[start] = 0
    
    while len(heap) != 0:
        
        min_dist, min_index = heapq.heappop(heap)
        
        if dist[min_index] < min_dist:
            continue
        
        for target_index, target_dist in graph[min_index]:
            new_dist = min_dist + target_dist
            
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist
                heapq.heappush(heap, (new_dist, target_index))
    
    return dist
    
# 입력
import sys, math, heapq
input = sys.stdin.readline

n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
   
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
a,b = map(int,input().split())

# 계산1: 다익스트라 3번
dist_1 = dijkstra(1)
dist_a = dijkstra(a)
dist_b = dijkstra(b)

# 계산2: 1번 경로, 2번경로
min_a_b = dist_1[a] + dist_a[b] + dist_b[n]
min_b_a = dist_1[b] + dist_b[a] + dist_a[n]

# 출력: 최소경로 구하기
min_res = min(min_a_b, min_b_a)
if min_res == math.inf:
    print(-1)
else:
    print(min_res)