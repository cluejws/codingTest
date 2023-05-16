import math

def solution(n, results):
        
    # 계산1: 플로이드 와샬
    dist = [[math.inf for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        dist[i][i] = 0
    
    for res in results:
        a, b = res
        dist[a][b] = min(dist[a][b], 1)
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    # 계산2: 번호 순회
    res = 0
    for i in range(1, n+1):
        
        # 1. 개수 세기
        cnt = 0
        for j in range(1, n+1):
            if dist[i][j] == math.inf and dist[j][i] == math.inf:
                continue
            else:
                cnt += 1
    
        # 2. 개수 판단
        if cnt == n:
            res += 1
    
    return res