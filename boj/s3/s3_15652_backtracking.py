def getResult():
    
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        
        if len(arr) != 0 and arr[-1] > i:
            continue
        
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