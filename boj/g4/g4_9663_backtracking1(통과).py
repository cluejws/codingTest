def check(cnt, i):
    

    for j in range(cnt):
        
        if (cnt - j) == abs(i - graph[j]) or i == graph[j]: 
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

# 계산
graph = [-1 for _ in range(n)]
res = 0
getResult(0)

# 출력
print(res)