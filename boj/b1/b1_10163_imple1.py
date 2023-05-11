# 입력
import sys
input = sys.stdin.readline

n = int(input())
graph = [[0 for _ in range(1001)] for _ in range(1001)]

# 계산1 및 입력: 방문처리
for k in range(n):
    x, y, w, h = list(map(int,input().split()))
    for i in range(1000-y, 1000-y-h, -1):
        for j in range(x, x+w):
            graph[i][j] = k + 1

# 계산2 및 출력: 방문처리 개수 세기
for k in range(1, n+1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if graph[i][j] == k:
                cnt += 1
    print(cnt)