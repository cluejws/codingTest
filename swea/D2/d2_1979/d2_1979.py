import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(t):

    # 입력
    n, k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    # 계산
    cnt = 0

    # 계산1: 세로
    for j in range(n):
        for i in range(n-k+1):
            # x-1: 범위 작 or 0
            if i-1 < 0:
                pass
            else:
                if arr[i-1][j] == 1:
                    continue

            # x: 세팅
            isBreak = False
            for x in range(i, i+k):
                if arr[x][j] == 0:
                    isBreak = True
                    break

            if isBreak:
                continue

            # x+k: 범위 크 or 0
            if i+k >= n:
                pass
            else:
                if arr[i+k][j] == 1:
                    continue

            #print(f'세로 어떻게됨', i, j)
            cnt += 1

    # 계산2: 가로
    for i in range(n):
        for j in range(n-k+1):
            # y-1: 범위 작 or 0
            if j-1 < 0:
                pass
            else:
                if arr[i][j-1] == 1:
                    continue

            # y: 세팅
            isBreak = False
            for y in range(j, j + k):
                if arr[i][y] == 0:
                    isBreak = True
                    break

            if isBreak:
                continue

            # y+k: 범위 크 or 0
            if j+k >= n:
                pass
            else:
                if arr[i][j+k] == 1:
                    continue

            #print(f'가로 어떻게됨', i, j)
            cnt += 1

    # 출력
    print(f'#{tc+1} {cnt}')