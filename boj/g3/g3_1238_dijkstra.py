def getBackDijkstra(x):
    
    heap = []
    dist = [math.inf for _ in range(n+1)]
    
    # 계산1: 초기화
    dist[x] = 0 
    heapq.heappush(heap, (0, x))
    
    # 계산2: 다익스트라
    while len(heap) != 0:
        
        min_dist, min_index = heapq.heappop(heap)
        
        if dist[min_index] < min_dist:
            continue
        
        for target_index, target_dist in back_graph[min_index]:
            
            new_dist = min_dist + target_dist
            
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist
                heapq.heappush(heap, (new_dist, target_index))
    
    return dist  

def getGoDijkstra(x):
    
    heap = []
    dist = [math.inf for _ in range(n+1)]
    
    # 계산1: 초기화
    dist[x] = 0 
    heapq.heappush(heap, (0, x))
    
    # 계산2: 다익스트라
    while len(heap) != 0:
        
        min_dist, min_index = heapq.heappop(heap)
        
        if dist[min_index] < min_dist:
            continue
        
        for target_index, target_dist in go_graph[min_index]:
            
            new_dist = min_dist + target_dist
            
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist
                heapq.heappush(heap, (new_dist, target_index))
    
    return dist  

# 단방향 그래프: 입력
import sys, heapq, math
input = sys.stdin.readline

n,m,x = map(int,input().split())
back_graph = [[] for _ in range(n+1)]
go_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    back_graph[a].append((b,c))
    go_graph[b].append((a,c))
    
# 계산1: x -> 각 지점 까지의 최단거리  
min_back_dist = getBackDijkstra(x)

# 계산2: 각 지점 -> x 까지의 최단거리
min_go_dist = getGoDijkstra(x)

# 계산3: 최대 합 구하기
max_dist = 0
for i in range(1, n+1):
    max_dist = max(max_dist, min_go_dist[i] + min_back_dist[i])

# 출력
print(max_dist)