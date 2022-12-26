def bfs(index, end):

    visited = [-1 for _ in range(n+1)]
    
    queue = deque()
    queue.append(index)
    visited[index] = 0
    
    while len(queue) != 0:
        
        cur = queue.popleft()
        
        if cur == end:
            return visited[cur]
        
        for k in range(len(graph[cur])):
            y = graph[cur][k]
            if visited[y] == -1:
                
                visited[y] = visited[cur] + 1
                queue.append(y)
            
from collections import deque
import math

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

min_value = math.inf
min_index = math.inf 
for index in range(1,n+1):
    

    value = 0
    for end in range(1,n+1):
        
        if index == end:
            continue
        
        cnt = bfs(index,end)
        #print(f'{index} -> {end} : {cnt}')
        value += cnt
    #print(f'{index}의 총합 : {value}')
    
    if min_value > value:
        min_value = value
        min_index = index
    elif min_value == value:
        if min_index > index:
            min_index = index

# 출력
print(min_index)