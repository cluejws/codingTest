def check(x,y,n):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False

def getCount(l, n):
    
    group = 0
    
    # 계산1: temp_graph 생성
    temp_graph = [[1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= l:
                temp_graph[i][j] = 0
    
    # 계산2: 여러번 bfs
    visited = [[False for _ in range(n)] for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(n):
        for j in range(n):

            if visited[i][j] == False and temp_graph[i][j] == 1:
                
                group += 1    # 그룹 만들어서 반영
                queue = deque()
                queue.append((i,j))
                visited[i][j] = True
                
                while len(queue) != 0:
                    
                    cur_x, cur_y = queue.popleft()
                    for k in range(4):
                        next_x = cur_x + dx[k]
                        next_y = cur_y + dy[k]
                        
                        if check(next_x, next_y, n) and visited[next_x][next_y] == False and temp_graph[next_x][next_y] == 1:
                            visited[next_x][next_y] = True
                            queue.append((next_x, next_y))
            
    return group
    
# 입력
from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

# 계산1: 최대 가능 강수량
limit = 0
for g in graph:
    max_g = max(g)
    limit = max(limit, max_g)

# 계산2: (최대 가능 강수량)물 주면서 개수 판단
max_cnt = 0
for l in range(limit+1):
    cnt = getCount(l, n)
    max_cnt = max(cnt, max_cnt)
    
# 출력
print(max_cnt)