# 입력
import sys, math
input = sys.stdin.readline

n = int(input())

dist = [[math.inf for _ in range(n)] for _ in range(n)]

# 계산1: dist 자기자신 -> 자기자신 초기화 
# 직접 갈 수 있는 간선은 없어서 초기화X

# 계산2: 입력으로 dist 인접행렬화
for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(len(arr)):
        if arr[j] == 1:
            dist[i][j] = min(dist[i][j], 1)
    
# 계산3: 플로이드 와샬 
for k in range(n):
    for i in range(n):
        for j in range(n):
            
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 출력           
for i in range(n):
    for j in range(n):
        
        if dist[i][j] == math.inf:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()