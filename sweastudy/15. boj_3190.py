from collections import deque

def check(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else: 
        return False

# 입력(길:0 사과:2 뱀:3)
n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
    
k = int(input())
for _ in range(k):
    i,j = map(int,input().split())
    graph[i-1][j-1] = 2

# 입력
# 바라보는 방향에서 왼쪽:L 오른쪽:D
dir_arr = []
l = int(input())
for _ in range(l):
    ip = input().split()
    dir_arr.append((int(ip[0]),ip[1]))

# 계산
# 현재 방향: 상(0) 하(1) 좌(2) 우(3) = dir
# 현재 걸린시간: time

# 현재 머리 : start_x, start_y
# 현재 뱀 구조: queue
dir = 3
time = 0

start_x,start_y = 0,0
queue = deque()

queue.append((start_x,start_y))
graph[start_x][start_y] = 3
while True:
    
    #1. 시간변화
    time += 1 

    #2. 시간변화 후 뱀 변화  
    if dir == 0:
        start_x -= 1
        
        if check(start_x,start_y):
            if graph[start_x][start_y] == 0:      # 사과X
                
                queue.append((start_x,start_y))
                graph[start_x][start_y] = 3
                
                pop_x, pop_y = queue.popleft()
                graph[pop_x][pop_y] = 0

            elif graph[start_x][start_y] == 2:    # 사과O
                
                queue.append((start_x,start_y))
                graph[start_x][start_y] = 3

            else:                                 # 자신 몸
                break
        else:                                     # 벽
            break
            
    elif dir == 1:
        start_x += 1
        
        if check(start_x,start_y):
            if graph[start_x][start_y] == 0:     # 사과X
                
                queue.append((start_x,start_y))
                graph[start_x][start_y] = 3
                
                pop_x, pop_y = queue.popleft()
                graph[pop_x][pop_y] = 0

            elif graph[start_x][start_y] == 2:   # 사과O
                
                queue.append((start_x,start_y))
                graph[start_x][start_y] = 3

            else:                                # 자신 몸
                break
        else:                                    # 벽
            break
    
    elif dir == 2:
        start_y -= 1
        
        if check(start_x,start_y):
            if graph[start_x][start_y] == 0:     # 사과X
                
                queue.append((start_x,start_y))                
                graph[start_x][start_y] = 3

                pop_x, pop_y = queue.popleft()
                graph[pop_x][pop_y] = 0

            elif graph[start_x][start_y] == 2:   # 사과O
                
                queue.append((start_x,start_y))
                graph[start_x][start_y] = 3

            else:                                # 자신 몸
                break
        else:                                    # 벽
            break
    
    else:
        start_y += 1
        if check(start_x,start_y):
            
            if graph[start_x][start_y] == 0:     # 사과X
                
                queue.append((start_x,start_y))                
                graph[start_x][start_y] = 3

                pop_x, pop_y = queue.popleft()
                graph[pop_x][pop_y] = 0

            elif graph[start_x][start_y] == 2:   # 사과O
                
                queue.append((start_x,start_y))
                graph[start_x][start_y] = 3

            else:                                # 자신 몸
                break
        else:                                    # 벽
            break
    
    
    # 3. 뱀 변화후 방향 변화
    for d in dir_arr:
        
        if time < d[0]:
            break
        
        elif time == d[0]:
            if dir == 0:
                if d[1] == 'L':
                    dir = 2
                else:
                    dir = 3
            elif dir == 1:
                if d[1] == 'L':
                    dir = 3
                else:
                    dir = 2
            elif dir == 2:
                if d[1] == 'L':
                    dir = 1
                else:
                    dir = 0
            else:
                if d[1] == 'L':
                    dir = 0
                else:
                    dir = 1
    
# 출력
print(time)