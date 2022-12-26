def check(x,y):
    global n,m
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

def dfs(x,y):
    
    visited[x][y] = True
    
    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]
        
        if check(temp_x,temp_y) and graph[temp_x][temp_y] == 1:
            if visited[temp_x][temp_y] == False:
                dfs(temp_x,temp_y)
                
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(t):
    n,m,k = map(int,input().split())
    
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        a,b = map(int,input().split())
        graph[a][b] = 1
    
    cnt = 0    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == False:
                dfs(i,j)
                cnt += 1
    print(cnt)