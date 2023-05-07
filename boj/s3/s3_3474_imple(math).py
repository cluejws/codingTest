# 입력
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):

    # 입력
    n = int(input())
    temp = 5

    # 계산
    cnt = 0
    while temp <= n:
        cnt += (n // temp)
        temp *= 5

    # 출력
    print(cnt)