def check(cnt, i):
    
    # 계산1: 같은 열 존재 -> False    
    # 계산2: 기울기 대각선 존재 -> False
    for k in range(cnt):
        
        if arr[k] == i or abs(i - arr[k]) == abs(cnt - k):
            return False

    return True

def getResult(cnt):
    
    if cnt == n:
        global res
        res += 1
        #print(*arr)
        return 
       
    for i in range(n):
        
        if arr[cnt] == -1 and check(cnt, i):
            arr[cnt] = i
            getResult(cnt + 1)
            arr[cnt] = -1

import sys
input = sys.stdin.readline

n = int(input())
arr = [-1 for _ in range(n)]

# 계산: 백트래킹
res = 0
getResult(0)

# 출력
print(res)