# 입력
import sys, math
input = sys.stdin.readline

n = int(input())
m = int(input())

# 계산1: 플로이드 와샬 초기화
dist = [[math.inf for _ in range(n)] for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

# 계산2: 플로이드 와샬 초기화(입력)
for _ in range(m):
    a,b,c = map(int,input().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)
    
# 계산3: 플로이드 와샬
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 계산4: 갈 수 없는 경우 처리
for i in range(n):
    for j in range(n):
        if dist[i][j] == math.inf:
            dist[i][j] = 0

# 출력
for d in dist:
    print(*d)