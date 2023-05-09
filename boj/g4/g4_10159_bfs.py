def heavy_bfs(x):
    visited = [False for _ in range(n+1)]
    visited[x] = True

    queue = deque()
    queue.append(x)
    while len(queue) > 0:
        data = queue.popleft()
        for y in heavy[data]:
            if visited[y] == False:
                queue.append(y)
                visited[y] = True

    return visited

def light_bfs(x):
    visited = [False for _ in range(n+1)]
    visited[x] = True

    queue = deque()
    queue.append(x)
    while len(queue) > 0:
        data = queue.popleft()
        for y in light[data]:
            if visited[y] == False:
                queue.append(y)
                visited[y] = True

    return visited

# 입력
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 입력(bfs 자식으로=아래로 진행, bfs 부모로=위로 진행)
heavy = [[] for _ in range(n+1)]
light = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    heavy[a].append(b)
    light[b].append(a)

# 계산 및 출력: 모든 정점에서 bfs -> 각 정점 판단
for i in range(1, n+1):
    all_visited = [False for _ in range(n+1)]
    
    # 1. bfs 자식으로=아래로 진행
    heavy_visited = heavy_bfs(i)
    for j in range(1, n+1):
        if heavy_visited[j] == True:
            all_visited[j] = heavy_visited[j]

    # 2. bfs 부모로=위로 진행
    light_visited = light_bfs(i)
    for j in range(1, n+1):
        if light_visited[j] == True:
            all_visited[j] = light_visited[j]

    # 출력
    cnt = 0
    for j in range(1, n+1):
        if all_visited[j] == False:
            cnt += 1
    print(cnt)