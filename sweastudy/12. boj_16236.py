from collections import deque
import math

def check(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False

def bfs():
    
    # bfs
    queue = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]

    global sha_i,sha_j, shark_level
    visited[sha_i][sha_j] = 0
    queue.append((sha_i,sha_j))
    
    while len(queue) != 0:
        
        cur_x , cur_y = queue.popleft()
        
        for i in range(4):

            temp_x = cur_x + dx[i]
            temp_y = cur_y + dy[i]
            
            if check(temp_x,temp_y) and visited[temp_x][temp_y] == -1:
                
                # 상어의 크기보다 크면          지나감x, 
                # 상어의 크기보다 같거나 작으면  지나감o
                if graph[temp_x][temp_y] <= shark_level:  
                
                    queue.append((temp_x,temp_y))
                    visited[temp_x][temp_y] = visited[cur_x][cur_y] + 1
                    
    return visited

def get_minDist(dist):

    min_x = 0
    min_y = 0
    min_dist = math.inf
    

    global shark_level
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= graph[i][j] < shark_level: # 지나간곳O, 자기보다 작은 먹이들
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    min_x = i
                    min_y = j
                elif dist[i][j] == min_dist:
 
                    if i < min_x:
                        min_dist = dist[i][j]
                        min_x = i
                        min_y = j
                        
                    elif i == min_x:
                        
                        if j < min_y:
                            min_dist = dist[i][j]
                            min_x = i
                            min_y = j 
                            
    if min_dist == math.inf:            # 먹을먹이가 x
        return -1
    else:
        graph[min_x][min_y] = 0         # 먹을먹이가 o(최소거리먹이)
        return (min_x, min_y, min_dist) 
    
     
# 입력
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 먹이개수, 상어 위치 구하기
eat_cnt = 0         # 먹이 개수

sha_i, sha_j = 0,0  # 상어 위치(i,j) 
shark_level = 2     # 상어 크기
shark_exp = 0       # 상어 경험치

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sha_i, sha_j = i,j
        elif graph[i][j] != 0:
            eat_cnt += 1
            
# Level=9일때 문제가 되므로 상어시작위치-> 0
graph[sha_i][sha_j] = 0 
    
# 계산
time = 0

while eat_cnt != 0:
    
    dist = bfs()                           #계산1 -> bfs를 통해 거리계산
    min_info = get_minDist(dist)           #계산2 -> 최소거리계산(최소거리,최대로 위쪽으로,최대로왼쪽으로) 
    
    if min_info == -1:                     #먹이 다 먹기전에 끝
        break
    else:                           
        
        cur_x, cur_y, cur_dist = min_info  #계산3 -> 최소거리위치,최소거리경험치,최소거리
        
        sha_i, sha_j = cur_x, cur_y          #상어위치: 최소거리로 할당

        shark_exp += 1                       #상어경험치: 레벨업 해주기 
        if shark_level == shark_exp:
            shark_level += 1
            shark_exp = 0
        
        time += cur_dist                     #현재까지 걸린시간
        
        eat_cnt -= 1                       #계산4 -> while문을 위한 먹이 하나씩 줄이기
        
# 출력
print(time)

