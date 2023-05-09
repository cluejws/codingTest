def bfs(i):
    visited = [-1 for _ in range(n)]
    visited[i] = 0

    queue = deque()
    queue.append((i,0))
    while len(queue) > 0:
        data, depth = queue.popleft()
        for y in graph[data]:
            if visited[y] == -1:
                queue.append((y, depth+1))
                visited[y] = depth + 1
    
    return visited

# 입력
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
line = [list(input().rstrip()) for _ in range(n)]

# 계산1: 그래프 생성
graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(i+1, n): 
        if line[i][j] == 'Y':
            graph[i].append(j)
            graph[j].append(i)

# 계산2: 모든 정점에서 bfs -> 최대값 구하기
max_res = 0
for i in range(n):
    
    # 1. bfs
    visited = bfs(i)
    
    # 2. 깊이1,2 개수 세기
    cnt = 0
    for v in visited:
        if v == 1 or v == 2:
            cnt += 1

    # 3. 최대값 구하기
    max_res = max(max_res, cnt)

# 출력
print(max_res)