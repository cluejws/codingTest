# 입력
import sys
input = sys.stdin.readline

n = int(input())
list_line = [tuple(map(int,input().split())) for _ in range(n)]

# 계산0: 정렬
list_line.sort(key=lambda x: (x[0]))

# 계산1: 시작점 초기화
min_cnt = 0
min_id = list_line[0][0]

left = 0
right = 0
for i in range(n):
    min_cnt += (list_line[i][0] - list_line[0][0]) * (list_line[i][1])
    right += list_line[i][1]

# 계산2: 슬라이딩 윈도우
for i in range(1, n):
    left += list_line[i-1][1]
    right -= list_line[i-1][1]

    temp_cnt = min_cnt + (list_line[i][0] - list_line[i-1][0]) * (left - right)
    if min_cnt > temp_cnt:
        min_cnt = temp_cnt
        min_id = list_line[i][0]

# 출력
print(min_id)