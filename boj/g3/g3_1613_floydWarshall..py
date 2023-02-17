# 입력
import sys, math
input = sys.stdin.readline

n, k = map(int,input().split())
dist = [[math.inf for _ in range(n+1)] for _ in range(n+1)]

# 계산0: 플로이드 와샬 초기화
for i in range(1, n+1):
    dist[i][i] = 0

# 계산1: (입력)플로이드 와샬 초기화
for _ in range(k):
    a,b = map(int,input().split())
    dist[a][b] = min(dist[a][b] , 1)

# 계산2: 플로이드 와샬
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 출력: (입력) 1, -1, 0
s = int(input())
for _ in range(s):
    
    a,b = map(int,input().split())
    #print(f'비교:{dist[a][b]}, {dist[b][a]}')
    
    if dist[a][b] == math.inf and dist[b][a] == math.inf:
        print(0)
        continue
    
    if dist[a][b] < dist[b][a]:
        print(-1)
    elif dist[a][b] > dist[b][a]:
        print(1)