import sys
from collections import deque 
input = sys.stdin.readline

def bfs(start,end):

    queue = deque()
    queue.append(start)
    visited[start] = 0
    
    while len(queue) != 0:

        current = queue.popleft()
        if current == end:
            return visited[current]

        go = current + 1        
        if check(go):
            
            if visited[go] == -1:
                queue.append(go)
                visited[go] = visited[current] + 1

        back = current - 1   
        if check(back):
            
            if visited[back] == -1:
                queue.append(back)
                visited[back] = visited[current] + 1

        mul = current * 2
        if check(mul):
            
            if visited[mul] == -1:
                queue.append(mul)
                visited[mul] = visited[current] + 1
          
def check(x):
    
    if 0<=x<=100000: return True
    else: return False   


n,k = map(int,input().split())
visited = [-1 for _ in range(100001)]
print(bfs(n,k))