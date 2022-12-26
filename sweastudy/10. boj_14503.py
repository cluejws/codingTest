def check(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

def step1(i,j):
    global res
    res += 1
    visited[i][j] = True

# 입력
n,m = map(int,input().split())
r,c,d= map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]   # 벽인지 아닌지 판단
visited = [[False for _ in range(m)] for _ in range(n)]      # 청소했는지 안했는지 판단

# 계산1(시작위치 청소)
res = 0    # 청소횟수
step1(r,c)

cnt = 0    # 청소기돌린횟수 = 4번까지
dir = d    # 현재 청소기방향
x,y = r,c  # 현재 청소기위치


# 계산2(움직이면서 청소)
while cnt <= 4:
    
    #print(f"({x},{y}) dir:{dir} cnt:{cnt}")
    if dir == 0:   # 북쪽
        
        #2-3,4 4방향 X => 후진, 종료
        if cnt == 4: 
            if check(x+1,y) and graph[x+1][y] == 0:
                x,y = x+1, y
                dir = 0 #북쪽에서 그대로방향=북쪽
                cnt = 0
            else:
                break
        
        #2-1: 범위O and 벽X(청소공간o) | 청소X
        if check(x,y-1) and graph[x][y-1] == 0 and visited[x][y-1] == False: 
            step1(x,y-1)
            x,y = x, y-1
            dir = 3 #북쪽에서 왼쪽방향=서쪽
            cnt = 0

        #2-2: 범위X or 벽O(청소공간x) | 청소O
        elif not check(x,y-1) or graph[x][y-1] == 1 or visited[x][y-1] == True: 
            dir = 3 #북쪽에서 왼쪽방향=서쪽
            cnt += 1
        
        
    elif dir == 1: # 동쪽
        
        #2-3,4 4방향 X => 후진, 종료
        if cnt == 4: 
            if check(x,y-1) and graph[x][y-1] == 0:
                x,y = x, y-1
                dir = 1 #동쪽에서 그대로방향=동쪽
                cnt = 0
            else:
                break

        #2-1: 범위O and 벽X(청소공간o) | 청소X
        if check(x-1,y) and graph[x-1][y] == 0 and visited[x-1][y] == False: 
            step1(x-1,y)
            x,y = x-1, y
            dir = 0 #동쪽에서 왼쪽방향=북쪽 
            cnt = 0
 
        #2-2: 범위X or 벽O(청소공간x) | 청소O
        elif not check(x-1,y) or graph[x-1][y] == 1 or visited[x-1][y] == True: 
            dir = 0 #동쪽에서 왼쪽방향=북쪽 
            cnt += 1          
            
    elif dir == 2: # 남쪽
        
        #2-3,4 4방향 X => 후진, 종료
        if cnt == 4: 
            if check(x-1,y) and graph[x-1][y] == 0:
                x,y = x-1, y
                dir = 2 #남쪽에서 그대로방향=남쪽
                cnt = 0
            else:
                break
        
        #2-1: 범위O and 벽X(청소공간o) | 청소X
        if check(x,y+1) and graph[x][y+1] == 0 and visited[x][y+1] == False: 
            step1(x,y+1)
            x,y = x, y+1
            dir = 1 #남쪽에서 왼쪽방향=동쪽 
            cnt = 0

        #2-2: 범위X or 벽O(청소공간x) | 청소O
        elif not check(x,y+1) or graph[x][y+1] == 1 or visited[x][y+1] == True: 
            dir = 1 #남쪽에서 왼쪽방향=동쪽 
            cnt += 1

            
    elif dir == 3: # 서쪽
        
        #2-3,4 4방향 X => 후진, 종료
        if cnt == 4: 
            if check(x,y+1) and graph[x][y+1] == 0:
                x,y = x,y+1
                dir = 3 #서쪽에서 그대로방향=서쪽
                cnt = 0
            else:
                break
        
        #2-1: 범위O and 벽X(청소공간o) | 청소X
        if check(x+1,y) and graph[x+1][y] == 0 and visited[x+1][y] == False: 
            step1(x+1,y)
            x,y = x+1, y
            dir = 2 #서쪽에서 왼쪽방향=남쪽 
            cnt = 0

        #2-2: 범위X or 벽O(청소공간x) | 청소O
        elif not check(x+1,y) or graph[x+1][y] == 1 or visited[x+1][y] == True:  
            dir = 2 #서쪽에서 왼쪽방향=남쪽 
            cnt += 1 

# 출력
print(res)