import sys
sys.stdin = open('1_input.txt', 'r')

import math

print_arr = []
t = int(input())
for tc in range(t):

    # 입력
    n = int(input())

    # 계산
    score = 0
    for _ in range(n):

        # 입력
        x, y = map(int,input().split())

        # 계산1: 반지름 얻기
        r = math.ceil(math.sqrt(x * x + y * y) / 20)

        # 계산2: 가장 가까운 원 찾기
        if r == 0:
            score += 10
            continue

        if r < 11:
            score += (11 - r)
        else:
            score += 0

    # 출력
    print_arr.append(f'#{tc+1} {score}')

# 출력
for pa in print_arr:
    print(pa)