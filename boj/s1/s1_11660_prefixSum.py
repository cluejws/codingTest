def getResult(x1,y1,x2,y2):
    if x1 == 0 and y1 == 0:
        return prefix_sum[x2][y2]
    elif x1 == 0 and y1 != 0:
        return prefix_sum[x2][y2] - prefix_sum[x2][y1 - 1]
    elif x1 != 0 and y1 == 0:
        return prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2]
    else: 
        return prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]

# 입력
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

# 계산: 누적합
prefix_sum = [[0 for _ in range(n)] for _ in range(n)]

# 계산1: 누적합 초기화
prefix_sum[0][0] = arr[0][0]

for i in range(1, n):
    prefix_sum[i][0] = prefix_sum[i-1][0] + arr[i][0]

for j in range(1,n):
    prefix_sum[0][j] = prefix_sum[0][j-1] + arr[0][j]

for i in range(1, n):
    for j in range(1, n):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + arr[i][j]


# 출력
for _ in range(m):
    
    x1,y1,x2,y2 = map(int,input().split())
    print(getResult(x1-1,y1-1,x2-1,y2-1))