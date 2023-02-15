def notStarResult(x,y,cnt):
    for i in range(x, x+cnt):
        for j in range(y, y+cnt):
            graph[i][j] = ' ' 

def getResult(x,y, cnt):
    if cnt == 1:
        return
    else:    
        getResult(x, y, cnt//3)
        getResult(x, y+cnt//3, cnt//3)
        getResult(x, y+(cnt//3)*2, cnt//3)
        getResult(x+cnt//3, y, cnt//3)
        
        getResult(x+cnt//3, y+cnt//3, cnt//3)
        notStarResult(x+cnt//3, y+cnt//3, cnt//3)

        getResult(x+cnt//3, y+(cnt//3)*2, cnt//3)
        getResult(x+(cnt//3)*2, y, cnt//3)
        getResult(x+(cnt//3)*2, y+cnt//3, cnt//3)
        getResult(x+(cnt//3)*2, y+(cnt//3)*2, cnt//3)
   
# 입력
import sys
input = sys.stdin.readline

n = int(input())

# 계산: 재귀
graph = [['*' for _ in range(n)] for _ in range(n)]
getResult(0, 0, n)

# 출력
for i in range(n):
    print(''.join(graph[i]))