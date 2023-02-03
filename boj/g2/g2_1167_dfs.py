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
sys.setrecursionlimit(10**4)

v = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(v):
    arr = list(map(int,input().split()))
    
    slice_arr = arr[1: len(arr)-1]
    for i in range(0, len(slice_arr), 2):
        graph[arr[0]].append((slice_arr[i], slice_arr[i+1]))


# 계산1: 임의의 루트노드1 에서 (가장 먼 노드) 구하기
# 단 -> 가장 먼 노드가 여러 개 있어도 한번 더 dfs 하기 때문에 상관x
visited = [-1 for _ in range(v+1)]
setResult(1, 0)

root_cost = max(visited)
root_index = -1
for i in range(1, v+1):
    if root_cost == visited[i]:
        root_index = i
        break

# 계산2: 가장 먼 노드에서 가장 먼 노드 까지의 (거리) 구하기
visited = [-1 for _ in range(v+1)]
setResult(root_index, 0)

max_cost = max(visited)

# 출력   
print(max_cost)