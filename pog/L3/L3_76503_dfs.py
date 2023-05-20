import sys
sys.setrecursionlimit(300000)

res = 0
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
    
    # 계산3: dfs
    def dfs(x):
        visited[x] = True
        for y in graph[x]:
            if visited[y] == False:
                
                # 1. dfs를 통해 leaf 노드 도달
                dfs(y)
        
                # 2. x(부모), y(자식)
                global res
                a[x] += a[y]
                res += abs(a[y])
                a[y] = 0
        
    visited = [False for _ in range(n)]
    dfs(0)

    return res