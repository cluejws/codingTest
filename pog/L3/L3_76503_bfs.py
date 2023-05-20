from collections import deque

def solution(a, edges):
    
    # 계산1: 가중치 합 = 0 판단
    if sum(a) != 0:
        return -1
    
    # 계산2: 그래프 생성
    n = len(a)
    graph = [[] for _ in range(n)]
    for edge in edges:
        nodeA, nodeB = edge
        graph[nodeA].append(nodeB)
        graph[nodeB].append(nodeA)

    # 계산3: root노드에서 경로 생성
    route = []
    
    queue = deque()
    visited = [False for _ in range(n)]
    visited[0] = True
    queue.append(0)
    
    while len(queue) > 0:
        x = queue.popleft()
        route.append(x)
        
        for y in graph[x]:
            if visited[y] == False:
                queue.append(y)
                visited[y] = True

    # 계산4: 경로에서 역순으로 누적 
    res = 0
    
    visited = [False for _ in range(n)]
    for i in range(n-1, -1, -1):
        x = route[i]
        visited[x] = True
        
        if a[x] != 0: 
            for y in graph[x]:
                if visited[y] == False:
                    a[y] += a[x]
                    res += abs(a[x])
                    a[x] = 0
          
    return res