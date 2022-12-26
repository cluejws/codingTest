import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    h , w , n = map(int,input().split())
    
    cnt = 0
    Y = n % h
    X = (n // h) + 1
    
    if n % h  == 0 :
        Y = h
        X = n // h

    print(Y * 100 + X)

    
