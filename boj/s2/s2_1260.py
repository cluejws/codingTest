import sys
from collections import deque

def DFS(graph, v, dfs_visited):
    dfs_visited[v] = True
    print(v, end=" ")
    
    for i in range(len(graph[v])):
        y = graph[v][i]
        if dfs_visited[y] == False:
            DFS(graph,y,dfs_visited)

def BFS(graph, v):
    bfs_visited = [False for _ in range(n+1)]
    queue = deque()
    
    queue.append(v)
    bfs_visited[v] = True
    print(v, end= " ")
    while len(queue) != 0:
        
        x = queue.popleft()
        for i in range(len(graph[x])):
            y = graph[x][i]
            if bfs_visited[y] == False:
                queue.append(y)
                bfs_visited[y]= True
                print(y, end =" ")
                

# 입력
input = sys.stdin.readline
n, m, v = map(int,input().split())

graph = [[] for _ in range(n+1)]
dfs_visited= [False for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(n+1):
    graph[i].sort()

# 출력
DFS(graph, v, dfs_visited)
print()
BFS(graph, v)