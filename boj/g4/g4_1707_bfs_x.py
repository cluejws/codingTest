def bfs(x):
    visited = [0 for _ in range(v+1)]
    visited[x] = 1

    queue = deque()
    queue.append((x, 1))
    while len(queue) > 0:
        data, group = queue.popleft()
        for y in graph[data]:
            if visited[y] == 0:
                visited[y] = -(group)
                queue.append((y, -group))

            elif visited[y] == group:
                return False

    return True

# 입력
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):

    # 1. 그래프 생성
    v, e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 2. 모두 연결이 되지 않는 그래프 / 모든 정점 방문필요
    flag = True
    for i in range(1, v+1):
        isDual = bfs(i)
        if not isDual:
            flag = False
            break
    
    # 출력
    print('YES' if flag else 'NO')