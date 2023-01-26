# 입력
import sys, heapq, math
input = sys.stdin.readline

v,e = map(int,input().split())

graph = [[] for _ in range(v+1)]
dist = [[math.inf for _ in range(v+1)] for _ in range(v+1)]
heap = []

# 계산1: 입력하면서 초기화
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    dist[a][b] = c
    
    heapq.heappush(heap, [c,a,b])
    
# 계산2: 변형 다익스트라
while len(heap) != 0:
    
    min_dist, min_start, min_end = heapq.heappop(heap)
    
    # 추가된 변형 코드
    # heap을 이용하기 때문에 처음 나온 사이클이 가장 비용이 작은 사이클
    if min_start == min_end:
        print(min_dist)
        quit()
    
    if dist[min_start][min_end] < min_dist:
        continue
    
    for target_end, target_dist in graph[min_end]:
        
        new_dist = min_dist + target_dist
        if dist[min_start][target_end] > new_dist:
            dist[min_start][target_end] = new_dist
            heapq.heappush(heap, [new_dist, min_start, target_end])

# 불가능 경우 출력
print(-1)