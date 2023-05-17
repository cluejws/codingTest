def check(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    
    return False

def bfs(i,j):

    cnt = 1
    visited[i][j] = True
    queue = deque()

    queue.append((i,j))
    while len(queue) > 0:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if check(next_x, next_y):
                if visited[next_x][next_y] == False and graph[next_x][next_y] == 1:
                    cnt += 1
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = True
    
    return cnt

# 입력
from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    a, b = map(int,input().split())
    graph[a-1][b-1] = 1

# 계산: 방문하지 않은 정점 -> bfs
# 연결된 최대값 구하기
dx = [1,0,-1,0]
dy = [0,1,0,-1]

max_cnt = 0
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if visited[i][j] == False and graph[i][j] == 1:
            cnt = bfs(i,j)
            max_cnt = max(max_cnt, cnt)

# 출력
print(max_cnt)