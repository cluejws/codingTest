import sys, math
input = sys.stdin.readline

# Elog(v^2) * v -> 다익스트라
# v^3 -> 플로이드 와샬
v, e = map(int,input().split())
dist = [[math.inf for _ in range(v+1)] for _ in range(v+1)]

# 계산1: 자기자신 -> 자기자신 경로 
# 없을 수도 있을 수도 있어 초기화 X

# 계산2: 입력을 통한 인접행렬 초기화
for _ in range(e):
    
    a,b,c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
    
# 계산3: 플로이드 와샬
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 계산4: 자기자신 -> 자기자신 경로 최소값 구하기
min_res = math.inf
for i in range(1, v+1):
    min_res = min(min_res, dist[i][i])

# 출력
if min_res == math.inf:
    print(-1)
else:
    print(min_res)