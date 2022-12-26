def check(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

def get_num():

    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque()

    #1: 방문처리 및 큐에넣기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                visited[i][j] = True
                queue.append((i,j))
            elif graph[i][j] == 1:
                visited[i][j] = True

    #2. bfs
    while len(queue) != 0:

        cur_x, cur_y = queue.popleft()

        for k in range(4):
            next_x = cur_x + dx[k]
            next_y = cur_y + dy[k]

            if check(next_x,next_y) and graph[next_x][next_y] == 0:
                if visited[next_x][next_y] == False:
                    visited[next_x][next_y] = True
                    queue.append((next_x,next_y))
    #3. 개수 세기
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False:
                cnt += 1
    return cnt

def dfs(cnt, next):

    # 기저조건1: 벽 3개 세우기
    global max_res
    if cnt == 3:
        num = get_num()
        if max_res < num:
            max_res = num
            return
        return

    # 계산
    for k in range(next, len(zero_arr)):

        cur_x, cur_y = zero_arr[k]

        graph[cur_x][cur_y] = 1
        dfs(cnt+1, k+1)
        graph[cur_x][cur_y] = 0

# 입력
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 바이러스, 빈칸
virus_arr = []
zero_arr = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus_arr.append((i,j))
        elif graph[i][j] == 0:
            zero_arr.append((i,j))

# 계산
max_res = 0
dfs(0,0)

print(max_res)