# 입력
import sys
input = sys.stdin.readline

n = int(input())
list_line = input().rstrip()

# 계산0: 빨, 파 구분
red = []
blue = []
for i in range(n):
    line = list_line[i]
    if line == 'R':
        red.append(i)
    elif line == 'B':
        blue.append(i)

# 계산1: 좌측으로 보내기
red_res = 0
blue_res = 0
if list_line[0] == 'R':

    cnt = 0
    for i in range(n):
        if list_line[i] != 'R':
            break

        cnt += 1

    red_res = len(red) - cnt
    blue_res = len(blue)

elif list_line[0] == 'B':

    cnt = 0
    for i in range(n):
        if list_line[i] != 'B':
            break

        cnt += 1

    blue_res = len(blue) - cnt
    red_res = len(red)

min_left_res = min(red_res, blue_res)

# 계산2: 우측으로 보내기
red_res = 0
blue_res = 0
if list_line[-1] == 'R':

    cnt = 0
    for i in range(n-1, -1, -1):
        if list_line[i] != 'R':
            break
        
        cnt += 1

    red_res = len(red) - cnt
    blue_res = len(blue)

elif list_line[-1] == 'B':
    
    cnt = 0
    for i in range(n-1, -1, -1):
        if list_line[i] != 'B':
            break

        cnt += 1

    blue_res = len(blue) - cnt
    red_res = len(red)

min_right_res = min(red_res, blue_res)

# 출력
print(min(min_left_res, min_right_res))