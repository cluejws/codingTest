def check(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False

def bfs(i, j, group):

    queue = deque()
    visited[i][j] = group
    queue.append((i,j))

    while len(queue) > 0:
        
        cur_x, cur_y = queue.popleft()
        for d in range(4):
            next_x = cur_x + dx[d]
            next_y = cur_y + dy[d]
            if check(next_x,next_y):
                if visited[next_x][next_y] == 0 and graph[next_x][next_y] == 1:
                    queue.append((next_x,next_y))
                    visited[next_x][next_y] = group

def getRightDist():

    queue = deque()
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    
    dist[0][0] = 0
    queue.append((0, 0))

    while len(queue) > 0:
        
        cur_x, cur_y = queue.popleft()
        for d in range(4):
            next_x = cur_x + dx[d]
            next_y = cur_y + dy[d]
            if check(next_x,next_y):
                if dist[next_x][next_y] == -1:
                    queue.append((next_x,next_y))
                    dist[next_x][next_y] = dist[cur_x][cur_y] + 1

    return dist

def getLeftDist():
    queue = deque()
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    
    dist[0][n-1] = 0
    queue.append((0, n-1))

    while len(queue) > 0:
        
        cur_x, cur_y = queue.popleft()
        for d in range(4):
            next_x = cur_x + dx[d]
            next_y = cur_y + dy[d]
            if check(next_x,next_y):
                if dist[next_x][next_y] == -1:
                    queue.append((next_x,next_y))
                    dist[next_x][next_y] = dist[cur_x][cur_y] + 1

    return dist

# 입력
from collections import deque
import sys, math
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 계산1: bfs(방문처리 통해 그룹화)
visited = [[0 for _ in range(n)] for _ in range(n)]
group = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j, group)
            group += 1

# 계산2: bfs(거리 생성)
rightDist = getRightDist()
leftDist = getLeftDist()

# 계산3: 최소 거리 얻기
min_dist = math.inf
for ax in range(n):
    for ay in range(n):
        for bx in range(n):
            for by in range(n):
                if visited[ax][ay] != 0 and visited[bx][by] != 0 and visited[ax][ay] != visited[bx][by]:
                    if ax >= bx and ay >= by:
                        min_dist = min(min_dist, abs(rightDist[ax][ay] - rightDist[bx][by]) - 1)
                    elif ax >= bx and ay <= by:
                        min_dist = min(min_dist, abs(leftDist[ax][ay] - leftDist[bx][by]) - 1)
                    elif ax <= bx and ay >= by:   
                        min_dist = min(min_dist, abs(leftDist[ax][ay] - leftDist[bx][by]) - 1)
                    elif ax <= bx and ay <= by:
                        min_dist = min(min_dist, abs(rightDist[ax][ay] - rightDist[bx][by]) - 1)

# 출력
print(min_dist)