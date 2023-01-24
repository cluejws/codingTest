def check(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False

def getNotResult(n):
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    visited = [[False for _ in range(n)] for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            
            if visited[i][j] == False:
                
                value = graph[i][j]
                queue = deque()
                queue.append((i,j))
                visited[i][j] = True
                
                while len(queue) != 0:
                    
                    cur_x, cur_y = queue.popleft()
                    
                    for k in range(4):
                        next_x = cur_x + dx[k]
                        next_y = cur_y + dy[k]

                        if check(next_x,next_y) and graph[next_x][next_y] == value and visited[next_x][next_y] == False:
                            visited[next_x][next_y] = True
                            queue.append((next_x, next_y))
                
                cnt += 1
    return cnt

def getResult(n):
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    visited = [[False for _ in range(n)] for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            
            if visited[i][j] == False:
                
                if graph[i][j] == 'R' or graph[i][j] == 'G':
                    queue = deque()
                    queue.append((i,j))
                    visited[i][j] = True

                    while len(queue) != 0:

                        cur_x, cur_y = queue.popleft()

                        for k in range(4):
                            next_x = cur_x + dx[k]
                            next_y = cur_y + dy[k]

                            if check(next_x,next_y) and (graph[next_x][next_y] == 'R' or graph[next_x][next_y] == 'G') and visited[next_x][next_y] == False:
                                visited[next_x][next_y] = True
                                queue.append((next_x, next_y))

                else:
                    queue = deque()
                    queue.append((i,j))
                    visited[i][j] = True

                    while len(queue) != 0:

                        cur_x, cur_y = queue.popleft()

                        for k in range(4):
                            next_x = cur_x + dx[k]
                            next_y = cur_y + dy[k]

                            if check(next_x,next_y) and (graph[next_x][next_y] == 'B') and visited[next_x][next_y] == False:
                                visited[next_x][next_y] = True
                                queue.append((next_x, next_y))
                    
                cnt += 1
                    
    return cnt


# 입력
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input()) for _ in range(n)]

# 계산: bfs 적록색약 X, bfs 적록색약 O
notRes = getNotResult(n)
res = getResult(n)

# 출력
print(notRes, res)