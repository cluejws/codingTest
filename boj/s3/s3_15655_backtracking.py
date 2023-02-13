def getResult(start):
    
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(start, len(line)):        
        arr.append(line[i])
        getResult(i+1)
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
getResult(0)