def getResult(a,b,c):
    
    if b == 1:
        return a % c

    else:
        if b % 2 == 0:
            return (getResult(a, b // 2, c) ** 2) % c
        else:
            return ((getResult(a, b // 2, c) ** 2) * a) % c

import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())
print(getResult(a,b,c))