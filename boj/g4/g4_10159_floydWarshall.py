# 입력
import sys, math
input = sys.stdin.readline

n = int(input())
m = int(input())

# 계산1: 플로이드 와샬 초기화(방향 존재)
dist = [[math.inf for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = min(dist[a][b], 1)
    
# 계산2: 플로이드 와샬
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 출력(부모에서 자식, 자식에서 부모 판단)
for i in range(1, n+1):

    cnt = 0
    for j in range(1, n+1):
        if dist[i][j] == math.inf and dist[j][i] == math.inf:
            cnt += 1

    print(cnt)