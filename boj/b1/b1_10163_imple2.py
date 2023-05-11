# 입력
import sys
input = sys.stdin.readline

n = int(input())
graph = [[0 for _ in range(1001)] for _ in range(1001)]

# 계산1 및 입력: 방문처리
for k in range(n):
    x, y, w, h = list(map(int,input().split()))
    for y in range(y, y+h):
        graph[y][x:(x+w)] = [k + 1] * w

# 계산2 및 출력: 방문처리 개수 세기
for k in range(1, n+1):
    cnt = 0
    for i in range(1001):
        cnt += graph[i].count(k)
    print(cnt)