def check(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

# 입력
import sys, math
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 계산(1.토마토 익은 곳 찾기, 안익은 곳 찾기)
queue = deque()
not_queue = []
for i in range(n):
    for j in range(m):
        
        if graph[i][j] == 1:
            queue.append((i,j))
            visited[i][j] = 0
        elif graph[i][j] == 0:
            not_queue.append((i,j))
        
# 계산(2.bfs)
while len(queue) !=0:
    
    cur_x, cur_y = queue.popleft()
    for i in range(4):
        temp_x = cur_x + dx[i]
        temp_y = cur_y + dy[i]
        
        if check(temp_x,temp_y) and graph[temp_x][temp_y] == 0:
            if visited[temp_x][temp_y] == -1:
                visited[temp_x][temp_y] = visited[cur_x][cur_y] + 1
                queue.append((temp_x,temp_y))
            else:
                visited[temp_x][temp_y] = min(visited[cur_x][cur_y] + 1, visited[temp_x][temp_y])
            

# 안익은 토마토에서만 최대값이 나오니까
max_num = 0
for nq in not_queue:
    x,y = nq
    if visited[x][y] == -1:
        print(-1)
        quit()
    else:
        if max_num < visited[x][y]:
            max_num = visited[x][y]

print(max_num)

