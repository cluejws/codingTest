def check(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

def bfs():
    queue = deque()
    queue.append((0,0,0))
    visited[0][0][0] = 1

    while len(queue) != 0:

        cur_x, cur_y, breakCount = queue.popleft()

        if cur_x == n-1 and cur_y == m-1:
            return visited[cur_x][cur_y][breakCount]
        
        for i in range(4):

            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if check(next_x, next_y):

                # 벽 깰수 있음O, 벽O
                # 벽 깰수 있음X, 벽O -> 불가
                if graph[next_x][next_y] == 1 and breakCount + 1 <= k:
                    if visited[next_x][next_y][breakCount + 1] == -1:
                        visited[next_x][next_y][breakCount + 1] = visited[cur_x][cur_y][breakCount] + 1
                        queue.append((next_x,next_y, breakCount + 1))


                # 벽 깰수 있음O, 벽X 
                # 벽 깰수 있음X, 벽X 
                if graph[next_x][next_y] == 0:
                    if visited[next_x][next_y][breakCount] == -1:
                        visited[next_x][next_y][breakCount] = visited[cur_x][cur_y][breakCount] + 1
                        queue.append((next_x,next_y, breakCount))

    return -1
    
# 입력
from collections import deque

n, m, k = map(int,input().split())
graph = [list(map(int,list(input()))) for _ in range(n)]
visited = [[[-1 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 계산: 최소값 구하기
print(bfs())