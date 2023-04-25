# 입력
import sys
input = sys.stdin.readline

n = int(input())
list_line = [tuple(map(int,input().split())) for _ in range(n)]

# 계산0: 정렬(좌표)
list_line.sort(key=lambda x: (x[0]))

# 계산1: 우체국 0부터 시작 / left:0, right:11
dist = 0
left , right = 0, 0
for i in range(n):
    dist += (list_line[i][0] - list_line[0][0]) * list_line[i][1]
    right += list_line[i][1]

# 계산2: 우체국 이동하면서 / 최소 거리의 위치 구하기
min_dist = dist
min_pos = list_line[0][0]
for i in range(1, n):

    left += list_line[i-1][1]
    right -= list_line[i-1][1]
    dist = dist + (left - right) * (list_line[i][0] - list_line[i-1][0])

    if min_dist > dist:
        min_dist = dist
        min_pos = list_line[i][0]

# 출력
print(min_pos)