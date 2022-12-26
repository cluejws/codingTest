def check(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False

def dfs(x,y, cnt, dir):
    
    global i,j
    #print(f"{x} {y} dir:{dir} {arr}")

    # 경우1 -> 같은방향으로 쭉쭉가기
    temp_x = x + dx[dir]
    temp_y = y + dy[dir]
    
    
    if dir == 3 and i == temp_x and j == temp_y:    # 기저 조건1 : dir=3 에서 쭉쭉가다가 시작점만날때 
        if cnt not in res: # 가능 경우의 수
            res.append(cnt) 
        return 
    
    if check(temp_x,temp_y) and graph[temp_x][temp_y] not in arr:
        
        arr.append(graph[temp_x][temp_y])
        dfs(temp_x,temp_y,cnt+1,dir)
        arr.pop()
    
    
    # 경우2 -> 방향꺾기
    if dir <= 2:
        next_x = x + dx[dir+1]
        next_y = y + dy[dir+1]
        
        if dir+1 == 3 and i == next_x and j == next_y: # 기저 조건2 : dir=2 에서 꺾자마자 바로 시작점만날때
            if cnt not in res: # 가능 경우의 수
                res.append(cnt) 
            return 
        
        if check(next_x,next_y) and graph[next_x][next_y] not in arr:
            
            arr.append(graph[next_x][next_y])
            dfs(next_x,next_y,cnt+1,dir+1)
            arr.pop()

    
import sys
input = sys.stdin.readline

t = int(input())
dx = [1, 1, -1,-1]
dy = [1,-1, -1, 1]

for k in range(t):
     
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]

    res = [] # 가능 경우의 수
    
    for i in range(n):
        for j in range(n):
            arr = [] # 같은 디저트의종류가 있으면 안됨 -> arr에 저장
            
            arr.append(graph[i][j]) 
            dfs(i,j,1,0) # (x,y, cnt, dir)
            arr.pop()

    
    if len(res) == 0:
        print(f'#{k+1} {-1}')
    else:
        print(f'#{k+1} {max(res)}')