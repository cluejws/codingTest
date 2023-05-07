# 입력
import sys
input = sys.stdin.readline

n = int(input())
list_line = input().rstrip()

# 계산0: 빨, 파 구분
red_cnt = 0
blue_cnt = 0
for line in list_line:
    if line == 'R':
        red_cnt += 1
    elif line == 'B':
        blue_cnt += 1

min_res = min(red_cnt, blue_cnt)

# 계산1: 좌측으로 보내기
cnt = 0
for i in range(n):
    if list_line[i] != list_line[0]:
        break

    cnt += 1

if list_line[0] == 'R':
    min_res = min(min_res, red_cnt - cnt)
else:
    min_res = min(min_res, blue_cnt - cnt)

# 계산2: 우측으로 보내기
cnt = 0
for i in range(n-1, -1, -1):
    if list_line[i] != list_line[-1]:
        break

    cnt += 1

if list_line[-1] == 'R':
    min_res = min(min_res, red_cnt - cnt)
else:
    min_res = min(min_res, blue_cnt - cnt)

# 출력
print(min_res)