import heapq, math

def getGraph(n, edge):
    
    graph = [[] for _ in range(n+1)]
    for e in edge:
        a, b = e
        graph[a].append((b,1))
        graph[b].append((a,1))
        
    return graph

def dijkstra(n, graph):
    
    dist = [math.inf for _ in range(n+1)]
    
    heap = []
    heapq.heappush(heap, (0, 1))
    dist[1] = 0
    
    while len(heap) > 0:
        
        min_dist, min_index = heapq.heappop(heap)
        
        if dist[min_index] < min_dist:
            continue
        
        for target_index, target_dist in graph[min_index]:
            new_dist = min_dist + target_dist
            if dist[target_index] > new_dist:
                dist[target_index] = new_dist
                heapq.heappush(heap, (new_dist, target_index))
    
    return dist
    
def solution(n, edge):
    
    # 계산1: 그래프 생성
    graph = getGraph(n, edge)
    
    # 계산2: 노드1 부터 거리
    dist = dijkstra(n, graph)
    
    # 계산3: 노드1 부터 최대 거리
    max_dist = 0
    for d in dist:
        if d == math.inf:
            continue
        
        max_dist = max(max_dist, d)
        
    # 계산4: 최대 거리 개수
    max_cnt = 0
    for d in dist:
        if max_dist == d:
            max_cnt += 1
    
    return max_cnt