import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(t):

    # 1. 입력
    n = int(input())

    # 2. 속도 계산
    d, s = 0, 0
    for _ in range(n):

        # 2-1: 입력
        arr = list(map(int,input().split()))

        # 2-2: 속도 계산
        # 0: 현재 속도 유지
        if arr[0] == 0:
            pass
        # 1: 가속
        elif arr[0] == 1:
            s += (arr[1] * 1)
        # 2: 감속
        elif arr[0] == 2:
            if s - (arr[1] * 1) >= 0:
                s -= (arr[1] * 1)
            else:
                s = 0

        # 2-3: 거리 계산
        d += (s * 1)

    # 출력
    print(f'#{tc+1} {d}')