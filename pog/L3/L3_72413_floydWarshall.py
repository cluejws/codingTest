from collections import deque
import math 

def floydWarshall(fares, n, s):
    
    dist = [[math.inf for _ in range(n+1)] for _ in range(n+1)]
    
    # 1. 초기화
    for i in range(1, n+1):
        dist[i][i] = 0
        
    for fare in fares:
        a,b,cost = fare
        dist[a][b] = min(dist[a][b], cost)
        dist[b][a] = min(dist[b][a], cost)
    
    # 2. 플로이드와샬
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

def solution(n, s, a, b, fares):
    
    # 계산1: 플로이드 와샬
    dist = floydWarshall(fares, n, s)

    # 계산2: 중간지점 순회
    # 중간지점=s -> 합승X
    # 중간지점=나머지 -> 합승O
    min_dist = math.inf
    for center in range(1, n+1):
        dist1 = dist[s][center] 
        dist2 = dist[center][a]
        dist3 = dist[center][b]
        min_dist = min(min_dist, dist1+dist2+dist3)
        
    return min_dist