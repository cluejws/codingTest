def getResult(k):
    
    if len(arr) == k:
        res.append(int(''.join(list(map(str,arr)))))
        return
    
    for i in range(9,-1,-1):
        if len(arr) > 0 and arr[-1] <= i:
            continue
        
        arr.append(i)
        getResult(k)
        arr.pop()

# 입력
import sys
input = sys.stdin.readline

n = int(input())

# 계산: 총 개수 구분 
# 10C1+10C2...10C10 = 2^10 - 1
if n > 1023:
    print(-1)
else:
    
    # 계산1: 백트래킹
    res = []
    
    arr = []
    for k in range(1, 10+1):
        getResult(k)
    
    # 계산2: 정렬
    res.sort()
    
    # 출력
    print(res[n-1])