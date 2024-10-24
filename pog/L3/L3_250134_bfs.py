from collections import deque

# 범위
def check(x, y, n, m):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

# 불만족 조건
def isWall(x, y, graph):
    return graph[x][y] == 5

def isVisited(x, y, visited):
    return visited[x][y]

def isOverlapped(x1, y1, x2, y2):
    return (x1, y1) == (x2, y2)
    
def isSwitched(cx1, cy1, nx1, ny1, cx2, cy2, nx2, ny2):
    return ((cx1, cy1) == (nx2, ny2)) and ((cx2, cy2) == (nx1, ny1))
    
def getResult(srx, sry, sbx, sby, graph):
    # bfs 초기화
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    n = len(graph)
    m = len(graph[0])
    
    queue = deque()
    red_visited = [[False for _ in range(m)] for _ in range(n)]
    blue_visited = [[False for _ in range(m)] for _ in range(n)]
    
    # bfs
    red_reached = False
    blue_reached = False
    queue.append((srx, sry, sbx, sby, red_visited, blue_visited, 0))
    while len(queue) != 0:
        # 1. pop
        crx, cry, cbx, cby, cr_visited, cb_visited, cnt = queue.popleft()
        nr_visited = [cr_visited[i][:] for i in range(n)]
        nb_visited = [cb_visited[i][:] for i in range(n)]
        nr_visited[crx][cry] = True
        nb_visited[cbx][cby] = True
        
        # 2. 기저조건
        if graph[crx][cry] == 3 and graph[cbx][cby] == 4:
            return cnt
        
        # 3. push  
        if graph[crx][cry] == 3:
            red_reached = True
            blue_reached = False
        elif graph[cbx][cby] == 4:
            red_reached = False
            blue_reached = True
        else:
            red_reached = False
            blue_reached = False

        for d in range(4):
            if blue_reached == True: # red만 움직임
                nrx = crx + dx[d]
                nry = cry + dy[d]
                if check(nrx, nry, n, m):
                    if not (isWall(nrx, nry, graph) or isVisited(nrx, nry, nr_visited) or isOverlapped(nrx, nry, cbx, cby)):
                        queue.append((nrx, nry, cbx, cby, nr_visited, nb_visited, cnt + 1))
                
            elif red_reached == True: # blue만 움직임
                nbx = cbx + dx[d]
                nby = cby + dy[d]
                if check(nbx, nby, n, m):
                    if not (isWall(nbx, nby, graph) or isVisited(nbx, nby, nb_visited) or isOverlapped(nbx, nby, crx, cry)):
                        queue.append((crx, cry, nbx, nby, nr_visited, nb_visited, cnt + 1))
             
            else:   # red, blue둘다 움직임
                nrx = crx + dx[d]
                nry = cry + dy[d]
                if check(nrx, nry, n, m):
                    if not (isWall(nrx, nry, graph) or isVisited(nrx, nry, nr_visited)):
                        for dd in range(4):
                            nbx = cbx + dx[dd]
                            nby = cby + dy[dd]
                            if check(nbx, nby, n, m):
                                if not (isWall(nbx, nby, graph) or isVisited(nbx, nby, nb_visited) 
                                        or isOverlapped(nrx, nry, nbx, nby)
                                        or isSwitched(crx, cry, nrx, nry, cbx, cby, nbx, nby)
                                    ):
                                    queue.append((nrx, nry, nbx, nby, nr_visited, nb_visited, cnt + 1))
    
    return 0

def solution(maze):
    n = len(maze)
    m = len(maze[0])
    
    # 1. red, blue 출발점
    s_red_x, s_red_y = -1, -1
    s_blue_x, s_blue_y = -1, -1
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                s_red_x, s_red_y = i, j
            elif maze[i][j] == 2:
                s_blue_x, s_blue_y = i,j
    
    # 2. red, blue 최소 움직임
    min_res = getResult(s_red_x, s_red_y, s_blue_x, s_blue_y, maze)
    return min_res