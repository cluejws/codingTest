def getLCM(m,n):
    
    gcd = getGCD(m,n)
    return (m * n) // gcd

def getGCD(m, n):
    
    while (n != 0):
        
        r = m % n
        
        m = n
        n = r
    
    return m


import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    # 입력
    m,n,x,y = map(int,input().split())
    
    # 계산1: 최소공배수 얻기
    ans = getLCM(m,n)
    end_i = ans // m
    end_j = ans // n
    
    # 계산2: 최소공배수/m , 최소공배수/n 까지 판단
    res = -1
    for i in range(end_i):
        break_flag = False  
        for j in range(end_j):
            print(m * i + x, n * j + y)
            if (m * i + x) == (n * j + y):
                break_flag = True
                res = m * i + x
                break
        
        if break_flag == True:
            break
    
    # 출력
    print(res)