def check(x, y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False

import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(t):

    # 입력
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]

    # 2.1: 계산 선언
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[False for _ in range(n)] for _ in range(n)]

    # 2.2: 계산 초기화
    x, y = 0, 0
    dir = 0
    cnt = 1

    arr[x][y] = cnt
    visited[x][y] = True

    # 2.3: 계산 반영
    for _ in range(n * n - 1):

        # 1. 방향 판단
        next_x = x + dx[dir]
        next_y = y + dy[dir]
        if not check(next_x,next_y) or visited[next_x][next_y] == True:
            dir = (dir + 1) % 4

        # 3. 방향 판단 후 반영 or 그냥 반영
        x = x + dx[dir]
        y = y + dy[dir]

        visited[x][y] = True
        cnt += 1
        arr[x][y] = cnt

    # 출력
    print(f'#{tc+1}')
    for i in range(n):
        print(*arr[i])