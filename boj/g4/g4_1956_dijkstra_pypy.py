# 입력
import sys, heapq, math
input = sys.stdin.readline

v,e = map(int,input().split())

graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

# Elog(v^2) * v -> 다익스트라
# v^3 -> 플로이드 와샬

# 계산1: v번 다익스트라
all_dist = []
for i in range(1, v+1):
    
    heap = []
    dist = [math.inf for _ in range(v+1)]
    
    # 계산1-1: 시작점에서 연결된 index 얻기
    # 시작점으로 돌아오는것이 최소가 아니므로 시작점 초기화 X
    for target_index, target_dist in graph[i]:
        heapq.heappush(heap, (target_dist, target_index))
        dist[target_index] = target_dist
    
    # 계산1-2: 다익스트라
    while len(heap) != 0:
        
        min_dist, min_index = heapq.heappop(heap)
        
        if dist[min_index] < min_dist:
            continue
        
        for target_index, target_dist in graph[min_index]:
            
            new_dist = dist[min_index] + target_dist
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist
                heapq.heappush(heap, (new_dist, target_index))
  
    # 계산1-3: 시작점에서 시작점까지 최단경로 값              
    all_dist.append(dist[i])

# 계산2: 최소값 dist
min_res = min(all_dist)

# 출력
if min_res == math.inf:
    print(-1)
else:
    print(min_res)