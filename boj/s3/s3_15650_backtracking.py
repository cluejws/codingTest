def getResult(start):
    
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(start, n+1):
        arr.append(i)
        getResult(i+1)
        arr.pop()

# 입력
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

# 계산
arr = []
getResult(1)