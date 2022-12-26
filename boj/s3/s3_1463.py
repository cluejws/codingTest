def getResult(n):
    queue = deque()
    queue.append(n)
    
    visited[n] = 0
    
    while len(queue) !=0 :
        x = queue.popleft()
        
        if x % 3 == 0:
            y = x // 3            
            
            if visited[y] == -1:
                queue.append(y)
                visited[y] = visited[x] + 1
            else:
                visited[y] = min(visited[y], visited[x]+ 1)
                
            if y == 1:
                break
        if x % 2 == 0:
            y = x // 2
            if visited[y] == -1:
                queue.append(y)
                visited[y] = visited[x] + 1
            else:
                visited[y] = min(visited[y], visited[x]+ 1)
                
            if y == 1:
                break
       
        y = x -1 
        if visited[y] == -1:
            queue.append(y)
            visited[y] = visited[x] + 1
        else:
            visited[y] = min(visited[y], visited[x]+ 1)
        
        if y == 1:
            break
    
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
visited = [-1 for _ in range(n+1)]
getResult(n)
print(visited[1])

