import sys
input = sys.stdin.readline

m,n = map(int,input().split())


for i in range(m,n+1):
    
    is_break = False
    for j in range(2,int(i ** 0.5)+1):
        if i % j == 0:
            is_break= True
            break
        else:
            pass

    if i == 1: pass
    elif not is_break: print(i)
