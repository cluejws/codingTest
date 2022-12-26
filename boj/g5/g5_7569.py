def check(z,x,y):
    if 0<=z<h and 0<=x<n and 0<=y<m:
        return True
    else:
        return False

def bfs(queue):
    # 2. BFS
    while len(queue) != 0:
        cz, cx, cy = queue.popleft()

        for i in range(6):    
            temp_z = cz + dz[i]
            temp_x = cx + dx[i]
            temp_y = cy + dy[i]

            if check(temp_z,temp_x,temp_y) and graph[temp_z][temp_x][temp_y] == 0:
                if visited[temp_z][temp_x][temp_y] == -1:
                    queue.append((temp_z,temp_x,temp_y))
                    visited[temp_z][temp_x][temp_y] = visited[cz][cx][cy] + 1
                else:
                    visited[temp_z][temp_x][temp_y] = min(visited[temp_z][temp_x][temp_y], visited[cz][cx][cy] + 1)

# 입력
import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int,input().split())
graph = [[list(map(int,input().split()))for _ in range(n)] for _ in range(h)]
visited = [[[-1 for _ in range(m)] for _ in range(n)] for _ in range(h)]

dz = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]

# 1. 익은 토마토 구하기
queue = deque()
not_queue = []
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                queue.append((z,x,y))
                visited[z][x][y] = 0
            elif graph[z][x][y] == 0:
                not_queue.append((z,x,y))

# 2. bfs
bfs()


# 3. 안익은 토마토에서 최대값이니까
max_temp = 0
for nq in not_queue:
    z,x,y = nq
    if visited[z][x][y] == -1:
        print(-1)
        quit()
    else:
        if max_temp < visited[z][x][y]:
            max_temp = visited[z][x][y]
print(max_temp)
