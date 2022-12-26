import sys
input = sys.stdin.readline

n = int(input())

cnt = 1
k = 1
while True:
    
    if n == 1:
        print(cnt)
        break

    k += 6 * cnt
    cnt += 1    
    if n-1 < k:
        print(cnt)
        break
