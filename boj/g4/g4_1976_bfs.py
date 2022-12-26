def bfs(start, end):
    
    visited = [False for _ in range(n)]
    queue = deque()
    
    queue.append(start)
    visited[start] = True
    
    while len(queue) != 0:
        data = queue.popleft()
        
        if data == end:
            return True
        
        for i in range(len(graph[data])):

            if graph[data][i] == 1 and visited[i] == False:
                visited[i] = True
                queue.append(i)
    
    return False

from collections import deque
n = int(input())
m = int(input())

# 입력
graph = [list(map(int,input().split())) for _ in range(n)]
path = list(map(int,input().split()))

# 계산1: 
# 시작, 끝 통해 연결 판단 
# 단 중간에 안되면 끝
for i in range(m-1):
    if not bfs(path[i]-1 , path[i+1]-1):
        print('NO')
        quit()

print('YES')