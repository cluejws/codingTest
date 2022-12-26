import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    arr = [i for i in range(1,n+1)]
    
    for x in range(k):
        for y in range(1,n):
            arr[y] += arr[y-1]
    print(arr[-1])    