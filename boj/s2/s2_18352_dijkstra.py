def dijkstra(k, x):
    
    # 계산1: 다익스트라
    dist = [math.inf for _ in range(n+1)]
    
    heap = []
    dist[x] = 0
    heapq.heappush(heap, (0, x))
    
    while len(heap) != 0:
        
        min_dist, min_index = heapq.heappop(heap)
        
        if dist[min_index] < min_dist:
            continue
        
        for target_index, target_dist in graph[min_index]:
            
            new_dist = min_dist + target_dist
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist
                heapq.heappush(heap, (new_dist, target_index))

    # 계산2: 시작점 x로부터 min_dist==k 경우 return
    k_dist = []
    for i in range(n+1):
        if dist[i] == k:
            k_dist.append(i)
            
    return k_dist
    
# 입력
import sys, math, heapq
input = sys.stdin.readline

n, m, k, x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b, 1))

# 계산1: 다익스트라
min_dist = dijkstra(k, x)

# 계산2: 오름차순 정렬
min_dist.sort()

# 출력
if len(min_dist) == 0:
    print(-1)
else:
    for md in min_dist:
        print(md)