def check(x,y):
    
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False


# dfs(0,0,1, 1) -> dfs(1,0,2, 1+2 ) -> dfs(2,0,3, 1+2+3) -> dfs(2,0,4, 1+2+3+4)
            #   -> dfs(0,-1,2, 1+3)
def dfs(x,y,cnt,sum):
    
    if cnt == 4:
        
        global res
        if sum >= res:
            res = sum   
        return
     
    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]
        
        if check(temp_x,temp_y) and visited[temp_x][temp_y] == False:
            
            # ㅗ, ㅏ, ㅜ ,ㅓ 인 경우
            if cnt == 2:
                visited[temp_x][temp_y] = True
                dfs(x,y, cnt+1, sum + graph[temp_x][temp_y])
                visited[temp_x][temp_y] = False
            
            visited[temp_x][temp_y] = True
            dfs(temp_x,temp_y, cnt+1, sum + graph[temp_x][temp_y])
            visited[temp_x][temp_y] = False

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

res = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,1,graph[i][j])
        visited[i][j] = False
print(res)
        