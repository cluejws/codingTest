from collections import deque

def check(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

def bfs(x,y):
    
    global rng_cnt
    
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    rng_cnt += 1
        
    while len(queue) != 0:
        
        cur_x, cur_y = queue.popleft()
    
        for k in range(4):
            temp_x = cur_x + dx[k]
            temp_y = cur_y + dy[k]

            if check(temp_x,temp_y) and graph[temp_x][temp_y] == 0:
                if visited[temp_x][temp_y] == False:
                    
                    rng_cnt += 1
                    visited[temp_x][temp_y] = True
                    queue.append((temp_x,temp_y))

# 입력
n,m,k = map(int,input().split())

# 직사각형 후보군을 통해 graph 만들기
graph = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [1,-1, 0,0]
dy = [0,0,1,-1]

arr = []
for _ in range(k):
    st_y, st_x , ed_y, ed_x = map(int,input().split())

    for i in range(n-ed_x, n-st_x):
        for j in range(st_y, ed_y):
            graph[i][j] = 1
            
# BFS통해 각 영역개수, 총 영역수
rng_arr = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == False:

            rng_cnt = 0
            bfs(i,j)
            rng_arr.append(rng_cnt)
 
# 정렬
rng_arr.sort()

# 출력
print(len(rng_arr))
print(' '.join(map(str,rng_arr)))
