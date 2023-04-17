# 입력
import sys
input = sys.stdin.readline

line = input().rstrip()

# 계산1: split
list_line = line.split('-')

# 계산2: - 있는 경우 / 없는 경우
n = len(list_line)
sum_res = 0
if n > 1:

    # 1. 시작점(덧셈)
    split_line = list_line[0].split('+')
    for sl in split_line:
        sum_res += int(sl)

    # 2. 나머지(뺄셈)
    for i in range(1, n):
        split_line = list_line[i].split('+')
        for sl in split_line:
            sum_res -= int(sl)
else:

    # 1. 시작점 ~ 나머지(덧셈)
    for i in range(n):
        split_line = list_line[i].split('+')
        for sl in split_line:
            sum_res += int(sl)

# 출력
print(sum_res)