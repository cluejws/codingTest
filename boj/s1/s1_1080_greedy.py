def changeGraph(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            if aGraph[x][y] == 1:
                aGraph[x][y] = 0
            elif aGraph[x][y] == 0:
                aGraph[x][y] = 1

def check():
    for x in range(n):
        for y in range(m):
            if aGraph[x][y] != bGraph[x][y]:
                return False
    
    return True

# 입력
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
aGraph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
bGraph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

# 계산1: 뒤집기
cnt = 0
for x in range(n-2):
    for y in range(m-2):
        if aGraph[x][y] != bGraph[x][y]:
            changeGraph(x, y)
            cnt += 1

# 계산2: 예외사항 판단
if check():
    print(cnt)
else:
    print(-1)