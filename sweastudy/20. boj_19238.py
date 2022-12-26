def check(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False

# 입력
from collections import deque

n,m,energy = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)] #길:0 벽:1
real_taxi_x, real_taxi_y = map(int,input().split())

son_arr = []
for _ in range(m):
    start_x, start_y, end_x, end_y = map(int,input().split())
    son_arr.append((start_x-1,start_y-1, end_x-1, end_y-1))

# 최단 거리 구하기
def getDist(taxi_x, taxi_y):
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[-1 for _ in range(n)] for _ in range(n)]    
    
    queue = deque()
    queue.append((taxi_x,taxi_y))
    
    visited[taxi_x][taxi_y] = 0
    
    while len(queue) != 0:
        
        cur_x , cur_y = queue.popleft()
        
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            
            if check(next_x,next_y) and graph[next_x][next_y] == 0:
                if visited[next_x][next_y] == -1:
                    visited[next_x][next_y] = visited[cur_x][cur_y] + 1
                    queue.append((next_x,next_y))
                else:
                    visited[next_x][next_y] = min(visited[next_x][next_y], visited[cur_x][cur_y] + 1)
    
    return visited

# 가장 가까운 손님 구하기
def getSon(dist):
    
    son0 = son_arr[0]
    res_start_x , res_start_y, res_end_x, res_end_y = son0
    
    distance = dist[res_start_x][res_start_y]
    index = 0

    for i in range(1, len(son_arr)):
        
        temp_start_x, temp_start_y, temp_end_x, temp_end_y = son_arr[i]
        
        if dist[temp_start_x][temp_start_y] < distance:
            index = i
            res_start_x = temp_start_x
            res_start_y = temp_start_y
            res_end_x = temp_end_x
            res_end_y = temp_end_y
            distance = dist[temp_start_x][temp_start_y]
            
        elif dist[temp_start_x][temp_start_y] == distance:
            
            if temp_start_x < res_start_x:
                index = i
                res_start_x = temp_start_x
                res_start_y = temp_start_y
                res_end_x = temp_end_x
                res_end_y = temp_end_y            
                distance = dist[temp_start_x][temp_start_y]

            elif temp_start_x == res_start_x:
                
                if temp_start_y < res_start_y:
                    index = i
                    res_start_x = temp_start_x
                    res_start_y = temp_start_y
                    res_end_x = temp_end_x
                    res_end_y = temp_end_y
                    distance = dist[temp_start_x][temp_start_y]
    
    pop_data = son_arr.pop(index)
    
    return (res_start_x, res_start_y, res_end_x, res_end_y)

# 출발지 -> 목적지 거리 구하기
def getMove(start_x, start_y, end_x, end_y):
    
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    
    queue = deque()
    queue.append((start_x,start_y))
    visited[start_x][start_y] = 0
    
    while len(queue) != 0:
        
        cur_x, cur_y = queue.popleft()
        if cur_x == end_x and cur_y == end_y:
            return visited[cur_x][cur_y]
        
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            
            if check(next_x,next_y) and graph[next_x][next_y] == 0:
                if visited[next_x][next_y] == -1:
                    visited[next_x][next_y] = visited[cur_x][cur_y] + 1
                    queue.append((next_x,next_y))
                else:
                    visited[next_x][next_y] = min(visited[next_x][next_y], visited[cur_x][cur_y] + 1)
    
    return -1
            
# 계산
cnt = len(son_arr)
taxi_x = real_taxi_x - 1
taxi_y = real_taxi_y - 1

while cnt != 0:
    
    cnt -= 1
    
    # 1. 최단거리 구하기
    dist = getDist(taxi_x, taxi_y)
    #print(dist)
    
    # 2. 최소 손님 얻기
    # (단: 벽때문에 못가는 손님이 있으면 -1) 
    # (단: 손님 데려다주는 동안 연료 x -1)
    min_son = getSon(dist)
    res_start_x, res_start_y, res_end_x, res_end_y = min_son

    if dist[res_start_x][res_start_y] == -1:
        print(-1)
        quit()
    
    energy -= dist[res_start_x][res_start_y]
    if energy < 0:
        print(-1)
        quit()
    #print(f'손님: ({res_start_x}, {res_start_y}) ({res_end_x},{res_end_y})')
    #print(f'{cnt}=> 손님찾으러감 : {energy}')
    
    
    # 3. 최소 손님 목적지 까지 거리 구하기
    move = getMove(res_start_x,res_start_y,res_end_x,res_end_y)
    
    energy -= move
    if energy < 0:
        print(-1)
        quit()
    #print(f'{cnt}=> 손님목적지감 : {energy}') 
    
    
    # 4. 연료 충전       
    energy += 2 * move
    taxi_x , taxi_y = res_end_x, res_end_y
    #print(f'{cnt}=> 충전함 : {energy}')

# 출력
print(energy)