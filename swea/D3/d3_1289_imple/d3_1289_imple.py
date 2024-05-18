import sys
sys.stdin = open("input.txt", "r")

# 입력
t = int(input())
for tc in range(t):

    # 입력
    codes = list(map(int,list(input())))
    n = len(codes)

    # 계산1: 변화 위치 얻기
    cnt_list = codes[:]

    # 계산2: 변화 위치 반영
    cnt = 0
    idx = 0
    while idx < n:

        # 2-1:
        # 홀수 -> 변화O
        # 짝수 -> 변화X
        if cnt_list[idx] % 2 != 0:
            # 1.
            cnt += 1

            # 2.
            for i in range(idx, n):
                cnt_list[i] += 1

        # 2-2: idx 반영
        idx += 1

    # 출력
    print(f'#{tc+1} {cnt}')