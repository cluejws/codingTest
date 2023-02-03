def setResult(start, sum_cost):
    
    # 계산: dfs
    visited[start] = sum_cost
    for i in range(len(graph[start])):
        next_v, next_c = graph[start][i]

        if visited[next_v] == -1:
            setResult(next_v, sum_cost+ next_c)
            

# 양방향 그래프: 입력
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

# 계산1: 루트노드 1에서 (가장 먼 노드) 구하기
# 단 -> 가장 먼 노드가 여러 개 있어도 한번 더 dfs 하기 때문에 상관x
visited = [-1 for _ in range(n+1)]
setResult(1, 0)

root_cost = max(visited)
root_index = -1
for i in range(1, n+1):
    if root_cost == visited[i]:
        root_index = i
        break
 
# 계산2: 가장 먼 노드에서 가장 먼 노드 까지의 (거리) 구하기
visited = [-1 for _ in range(n+1)]
setResult(root_index, 0)

max_cost = max(visited)

# 출력   
print(max_cost)