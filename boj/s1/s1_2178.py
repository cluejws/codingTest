def check(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False
    
def BFS():
    visited[0][0] = 1
    queue = deque()
    queue.append((0,0))
    
    while len(queue) != 0:
        
        x, y = queue.popleft()
        if x == n-1 and y == m-1:
            print(visited[n-1][m-1])
            break
        
        for i in range(4):
            temp_x = x + dir_x[i]
            temp_y = y + dir_y[i]
            
            if check(temp_x, temp_y) and graph[temp_x][temp_y] == 1:
                if visited[temp_x][temp_y] == -1:
                    visited[temp_x][temp_y] = visited[x][y] + 1
                    queue.append((temp_x,temp_y))
  
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
dir_x = [1,0,-1,0]
dir_y = [0,1,0,-1]
visited = [[-1 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().rstrip("\n"))))

BFS()
    
