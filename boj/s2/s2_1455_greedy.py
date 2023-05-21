def changeGraph(i,j):
    for x in range(i+1):
        for y in range(j+1):
            if graph[x][y] == 1:
                graph[x][y] = 0
            elif graph[x][y] == 0:
                graph[x][y] = 1

# 입력
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int,list(input().rstrip()))) for _ in range(n)]

# 계산
cnt = 0
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if graph[i][j] == 1:
            changeGraph(i,j)
            cnt += 1

# 출력
print(cnt)