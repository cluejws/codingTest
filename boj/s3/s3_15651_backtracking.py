def getResult():
    
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        arr.append(i)
        getResult()
        arr.pop()
    
# 입력
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

# 계산
arr = []
getResult()