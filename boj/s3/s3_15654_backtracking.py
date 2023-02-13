def getResult():
    
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(len(line)):
        if line[i] in arr:
            continue
        
        arr.append(line[i])
        getResult()
        arr.pop()

# 입력
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
line = list(map(int,input().split()))

# 계산1: 정렬
line.sort()

# 계산2: 백트래킹
arr = []
getResult()