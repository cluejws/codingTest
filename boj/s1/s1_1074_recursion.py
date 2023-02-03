def getResult(r,c, n):
    

    if n == 0:
        return
    else:
        global rank
        res = 2 ** n
        if 0<=r<(res//2) and 0<=c<(res//2):
            rank += (2** (2 * (n-1))) * 0
            getResult(r, c , n-1)

        elif 0<=r<(res//2) and (res//2)<=c<res:
            rank += (2** (2 * (n-1))) * 1
            getResult(r, c- (res//2),  n-1)

        elif (res//2)<=r<res and 0<=c<(res//2):
            rank += (2** (2 * (n-1))) * 2
            getResult(r - (res//2), c,  n-1)

        elif (res//2)<=r<res and (res//2)<=c<res:
            rank += (2** (2 * (n-1))) * 3
            getResult(r - (res//2), c - (res//2),  n-1)

# 입력   
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

n,r,c = map(int,input().split())

# 계산: 분할 & 정복
rank = 0
getResult(r,c, n)

# 출력
print(rank)