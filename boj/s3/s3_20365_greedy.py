# 입력
import sys
input = sys.stdin.readline

n = int(input())
list_alp = input().rstrip()

# 계산: 연속 시작 위치
blue = []
red = []

# 계산1: 0부터 초기화
if list_alp[0] == 'B':
    blue.append(0)
elif list_alp[0] == 'R':
    red.append(0)

# 계산2: 1부터 끝까지
for i in range(1, n):
    pre_alp = list_alp[i-1]
    cur_alp = list_alp[i]

    if pre_alp == 'R' and cur_alp == 'B':
        blue.append(i)
    elif pre_alp == 'B' and cur_alp == 'R':
        red.append(i)

# 계산3 및 출력: 최소값 + 1
print(min(len(blue), len(red)) + 1)