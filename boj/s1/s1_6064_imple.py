def getResult(m,n,x,y):
    
    k = x
    while k <= m * n:
    
        if ((k - x) % m == 0) and ((k-y) % n == 0):
            return k
        
        k += m
        
    return -1


import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    # 입력
    m,n,x,y = map(int,input().split())
    
    # 계산
    res = getResult(m,n,x,y)

    # 출력
    print(res)