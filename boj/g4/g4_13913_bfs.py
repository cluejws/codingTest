def check(x):
    if 0<=x<=100000:
        return True
    else:
        return False

def bfs(start, end):
    
    queue = deque()
    
    queue.append(start)
    visited[start] = 0
    parent[start] = start
    
    while len(queue) != 0:
        
        # 현재 점
        cur_point = queue.popleft()
        if cur_point == end:
            return
        
        # 다음 점
        next_point = cur_point + 1
        if check(next_point):
            if visited[next_point] == -1:
                queue.append(next_point)
                visited[next_point] = visited[cur_point] + 1
                parent[next_point] = cur_point

        next_point = cur_point - 1
        if check(next_point):
            if visited[next_point] == -1:
                queue.append(next_point)
                visited[next_point] = visited[cur_point] + 1
                parent[next_point] = cur_point

        next_point = cur_point * 2
        if check(next_point):
            if visited[next_point] == -1:
                queue.append(next_point)
                visited[next_point] = visited[cur_point] + 1
                parent[next_point] = cur_point

def getRoute(start, end):
    
    route = []
    for _ in range(visited[end]):
        route.append(end)
        end = parent[end]
    route.append(start)
    
    return route

# 입력
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())

# 계산: bfs
visited = [-1 for _ in range(100000+1)]
parent = [-1 for _ in range(100000+1)]
bfs(n,k)

# 출력1
print(visited[k])

# 출력2
route = getRoute(n,k)
route.reverse()
print(*route)