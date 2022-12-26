from collections import deque

def check_range(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else: return False

def get_num():     # 바이러스 퍼진 후 빈칸 개수
    
    # 바이러스 퍼지기
    queue = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(n): # 방문처리: 바이러스=2 벽=1
        for j in range(m):
            if graph[i][j] == 2:  
                queue.append((i,j))
                visited[i][j] = 2
            elif graph[i][j] == 1:
                visited[i][j] = 1
            
    while len(queue) != 0:
        
        cur_x, cur_y = queue.popleft()
        for k in range(4):
            temp_x = cur_x + dx[k]
            temp_y = cur_y + dy[k]
            
            if check_range(temp_x,temp_y) and graph[temp_x][temp_y] == 0: # 방문처리: 빈칸=0 -> 바이러스=2
                if visited[temp_x][temp_y] == 0: 
                    visited[temp_x][temp_y] = 2
                    queue.append((temp_x,temp_y)) 

    # 빈칸 계산
    num = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:  
                num += 1
    return num              
        
    

def dfs(cnt, next): # cnt: 벽3개세우기 num:안전영역 next: 후보군위한 인덱스
    
    # 기저조건1: 벽3개 세우기
    global max_res 
    if cnt == 3:
        num = get_num()
        if max_res < num:
            max_res = num
            return
        return

    
    for k in range(next, len(zero_arr)):
        
        cur_x, cur_y = zero_arr[k]
        
        graph[cur_x][cur_y] = 1
        dfs(cnt+1, k+1)
        graph[cur_x][cur_y] = 0
    
# 입력
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# 빈칸(벽 후보군), 바이러스 얻기
zero_arr = []
virus_arr = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_arr.append((i,j))
        elif graph[i][j] == 2:
            virus_arr.append((i,j))

# 계산
max_res = 0
dfs(0,0)

# 출력
print(max_res)
