# 입력
import sys, math
input = sys.stdin.readline

n,m,b = map(int,input().split())
arr = [list(map(int, input().split()))for _ in range(n)]

res = math.inf
res_height = -1

# 완전 탐색
for height in range(257):
    put = 0
    remove = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] < height:
                put += (height - arr[i][j])
            else: 
                remove += (arr[i][j] - height)

    if put <= (remove + b):
        if (put + remove * 2) <= res:
            res = put + remove * 2
            res_height = height

print(res, res_height)