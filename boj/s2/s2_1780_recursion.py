def getResult(x, y , n):
    
    global minusOne_cnt, zero_cnt, plusOne_cnt
    value = graph[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if value != graph[i][j]:
                getResult(x, y, n//3)
                getResult(x, y+n//3, n//3)
                getResult(x, y+(n//3)*2, n//3)
                
                getResult(x+(n//3), y, n//3)
                getResult(x+(n//3), y+n//3, n//3)
                getResult(x+(n//3), y+(n//3)*2, n//3)

                getResult(x+(n//3)*2, y, n//3)
                getResult(x+(n//3)*2, y+n//3, n//3)
                getResult(x+(n//3)*2, y+(n//3)*2, n//3)
                return

    if value == -1:
        minusOne_cnt += 1
    elif value == 0:
        zero_cnt += 1
    elif value == 1:
        plusOne_cnt += 1


# 입력
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

# 계산: 재귀를 통해 개수 세기
minusOne_cnt = 0
zero_cnt = 0
plusOne_cnt = 0

getResult(0, 0, n)

# 출력
print(minusOne_cnt)
print(zero_cnt)
print(plusOne_cnt)