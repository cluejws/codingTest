def check(x, y):
    if 0<=x<n and 0<=y<n:
        return True

    return False

def change(x, y, color):

    # 흑: 1
    if color == 1:
        for dir in range(8):

            # 계산1: 색칠 구간 얻기
            id_list = []
            isBreak = False

            dir_x = x
            dir_y = y
            for _ in range(n):
                dir_x = dir_x + dx[dir]
                dir_y = dir_y + dy[dir]

                # 1: 범위 판단
                if not check(dir_x, dir_y):
                    break

                # 2: 빈칸 판단
                if graph[dir_x][dir_y] == 0:
                    break

                # 3: 끝 판단
                if graph[dir_x][dir_y] == 1:
                    isBreak = True
                    break

                # 4. 추가(2)
                id_list.append((dir_x, dir_y))

            # 계산2: 색칠
            if isBreak == True:
                for id_x, id_y in id_list:
                    graph[id_x][id_y] = color

    # 백: 2
    elif color == 2:
        for dir in range(8):

            # 계산1: 색칠 구간 얻기
            id_list = []
            isBreak = False

            dir_x = x
            dir_y = y
            for _ in range(n):
                dir_x = dir_x + dx[dir]
                dir_y = dir_y + dy[dir]

                # 1: 범위 판단
                if not check(dir_x, dir_y):
                    break

                # 2: 빈칸 판단
                if graph[dir_x][dir_y] == 0:
                    break

                # 3. 끝 판단
                if graph[dir_x][dir_y] == 2:
                    isBreak = True
                    break

                # 4. 추가(1)
                id_list.append((dir_x, dir_y))

            # 계산2: 색칠
            if isBreak == True:
                for id_x, id_y in id_list:
                    graph[id_x][id_y] = color

    # 2. 반영
    graph[x][y] = color

import sys
sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(t):

    # 입력
    n, m = map(int,input().split())
    graph = [[0 for _ in range(n)] for _ in range(n)]

    # 계산0: 초기화
    temp = n // 2
    graph[temp-1][temp-1] = 2
    graph[temp-1][temp] = 1
    graph[temp][temp-1] = 1
    graph[temp][temp] = 2

    # 계산1: 흑 / 백 반영
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for _ in range(m):

        # 1-1: 입력
        i, j, c = map(int,input().split())

        # 1-2: 반영
        change(j - 1, i - 1, c)

    # 계산2: 흑 / 백 개수
    black = 0
    white = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                black += 1
            elif graph[i][j] == 2:
                white += 1

    # 출력
    print(f'#{tc + 1} {black} {white}')