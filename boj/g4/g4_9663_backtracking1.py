def check(x, y):
    
    # 계산1: 같은 열 존재 -> False    
    # 계산2: 기울기 대각선 존재 -> False
    for j in range(x):
        
        if y == graph[j] or (x - j) == abs(y - graph[j]):
            return False

    return True
        
def getResult(cnt):
    
    if cnt == n:
        global res
        res += 1
        return

    for i in range(n):  
        if check(cnt, i):
            graph[cnt] = i
            getResult(cnt + 1)
            graph[cnt] = -1

# 입력
import sys
input = sys.stdin.readline

n = int(input())
graph = [-1 for _ in range(n)]

# 계산: 백트래킹
res = 0
getResult(0)

# 출력
print(res)