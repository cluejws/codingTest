# 입력
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
list_pos = [tuple(map(int,input().split())) for _ in range(m)]

# 계산1: 각 차원 정렬
dimension = [[] for _ in range(n)]
for pos in list_pos:

    for i in range(n):
        dimension[i].append(pos[i])

for i in range(n):
    dimension[i].sort()

# 계산2: 각 차원의 최소 좌표
min_pos = []
for i in range(n):
    min_pos.append(dimension[i][m//2])

# 계산3: 각 차원의 최소 좌표 -> 각 차원의 거리 합의 총합
res = 0
for i in range(n):
    for j in range(m):
        res += abs(min_pos[i] - dimension[i][j])

# 출력
print(res)
print(*min_pos) 