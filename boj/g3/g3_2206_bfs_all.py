def check(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

# 입력
from collections import deque

n, m = map(int,input().split())
graph = [list(map(int,list(input()))) for _ in range(n)]
visited = [[[-1 for _ in range(2)] for _ in range(m)] for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]


# 계산: bfs
queue = deque()
queue.append((0,0,0))
visited[0][0][0] = 1

while len(queue) != 0:
    
    cur_x, cur_y, cur_isBreak = queue.popleft()
    if cur_x == n-1 and cur_y == m-1:
        break
    
    for i in range(4): 
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]

        if check(next_x, next_y):

            # 이전에 벽 부심X, 다음 벽 O  
            if cur_isBreak == 0 and graph[next_x][next_y] == 1:

                # 다음 벽을 부셔서, 1번씀
                if visited[next_x][next_y][1] == -1:
                    visited[next_x][next_y][1] = visited[cur_x][cur_y][cur_isBreak] + 1 
                    queue.append((next_x, next_y, 1))

            # 이전에 벽 부심X, 다음 벽 X
            # 이전에 벽 부심O, 다음 벽 x
            if graph[next_x][next_y] == 0:

                # 아직 벽을 안부셔서, 0번씀 
                # 이미 벽을 부셔서, 1번씀  
                if visited[next_x][next_y][cur_isBreak] == -1:
                    visited[next_x][next_y][cur_isBreak] = visited[cur_x][cur_y][cur_isBreak] + 1 
                    queue.append((next_x, next_y, cur_isBreak))

                    
# 출력
if visited[n-1][m-1][0] == -1 and visited[n-1][m-1][1] == -1:
    print(-1)
elif visited[n-1][m-1][0] == -1 or visited[n-1][m-1][1] == -1:
    print(max(visited[n-1][m-1][0], visited[n-1][m-1][1]))
else:
    print(min(visited[n-1][m-1][0], visited[n-1][m-1][1]))