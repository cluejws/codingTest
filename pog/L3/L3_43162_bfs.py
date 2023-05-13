from collections import deque

def bfs(computers, x, n):
    
    elements = []
    visited = [False for _ in range(n)]
    
    visited[x] = True
    queue = deque()
    queue.append(x)
    elements.append(x)
    
    while len(queue) > 0:
        data = queue.popleft()
        
        for y in range(n):
            if visited[y] == False and computers[data][y] == 1:
                visited[y] = True
                queue.append(y)
                elements.append(y)
                
    return elements
    
def solution(n, computers):
    
    # 계산1: 네트워크 얻기 -> 방문 안한 지점 bfs
    network = [-1 for _ in range(n)]
    for x in range(n):
        if network[x] == -1:
            elements = bfs(computers, x, n)
            for element in elements:
                network[element] = x
    
    # 계산2: 네트워크 세기 -> 네트워크 집합화
    set_network = set(network)

    # 출력
    return len(set_network)