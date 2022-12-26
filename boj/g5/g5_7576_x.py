def check(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

def bfs(x,y):
    
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    dist[x][y] = 0
    
    while len(queue) != 0:
        
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            temp_x = cur_x + dx[i]
            temp_y = cur_y + dy[i] 
            
            if check(temp_x,temp_y) and graph[temp_x][temp_y] == 0:
                if visited[temp_x][temp_y] == False:  # 방문처리X : queue넣기O, 방문처리O, dist최소로 넣기
                    queue.append((temp_x,temp_y)) 
                    visited[temp_x][temp_y] = True    
                    dist[temp_x][temp_y] = min(dist[temp_x][temp_y], dist[cur_x][cur_y] + 1)
                else:                                 # 방문처리O : dist최소로 넣기
                    dist[temp_x][temp_y] = min(dist[temp_x][temp_y], dist[cur_x][cur_y] + 1)
                

# 입력
import sys, math
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dist = [[math.inf for _ in range(m)] for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 계산(bfs: 토마토 익은 곳)
for i in range(n):
    for j in range(m):
        
        if graph[i][j] == 1:
            visited = [[False for _ in range(m)] for _ in range(n)]
            bfs(i,j)
        elif graph[i][j] == -1:
            dist[i][j] = -1
            

# 출력 : dist에서 최대값
max_num = -1
for i in range(n):
    for j in range(m):
        
        if dist[i][j] == math.inf:
            print(-1)
            quit()
        else:
            if max_num < dist[i][j]:
                max_num = dist[i][j]
print(max_num)