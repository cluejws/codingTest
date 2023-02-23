def getResult():
    
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            arr.append(i)
            getResult()
            arr.pop()
            visited[i] = False
    
# 입력
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

# 계산
arr = []
visited = [False for _ in range(n+1)]
getResult()