# 입력
import sys
input = sys.stdin.readline

n = int(input())
list_pos = [list(map(int,input().split())) for _ in range(n)]

# 계산1: x축 정렬, y축 정렬
sorted_x = sorted(list_pos, key= lambda x: x[0])
sorted_y = sorted(list_pos, key= lambda x: x[1])

# 계산2: 최소 위치 
min_x = sorted_x[n//2][0]
min_y = sorted_y[n//2][1]

# 계산3: 최소 위치 합
sum_res = 0
for i in range(n):
    x, y = list_pos[i]
    sum_res += (abs(min_x - x) + abs(min_y - y))

# 출력
print(sum_res)