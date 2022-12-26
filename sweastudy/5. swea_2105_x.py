def check(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False

def dfs(x,y, cnt):
    
    for d in range(4):
        temp_x = x + dx[d]
        temp_y = y + dy[d]
        
        # 기저조건 1
        global i,j
        if i == temp_x and j == temp_y:
            if cnt not in res:
                res.append(cnt) # 가능 경우의 수
            return
        
        if check(temp_x,temp_y) and graph[temp_x][temp_y] not in arr and visited[temp_x][temp_y] == False:
            
            visited[temp_x][temp_y] = True
            arr.append(graph[temp_x][temp_y])
            
            dfs(temp_x,temp_y,cnt+1)
            
            visited[temp_x][temp_y] = False
            arr.pop()


import sys
input = sys.stdin.readline

t = int(input())
dx = [1, 1, -1,-1]
dy = [1,-1, -1, 1]

for k in range(t):
     
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    res = [] # 가능 경우의 수
    
    for i in range(n):
        for j in range(n):
            arr = [] # 같은 디저트의종류가 있으면 안됨 -> arr에 저장
            
            visited[i][j] = True
            arr.append(graph[i][j])
            
            dfs(i,j,1) # (x,y, cnt)
            
            visited[i][j] = False
            arr.pop()
            
 
    print(f'#{k+1}: {res}')