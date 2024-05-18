def check():

    # 기울기: 1, -1 판단
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = i, temp[i]
            x2, y2 = j, temp[j]
            if (y2-y1) == (x2-x1):
                return False

            if (y2-y1) == -1 * (x2-x1):
                return False

    return True

def getResult():

    # 기저조건
    global cnt
    if len(temp) == n:

        # 1. 대각선 판단
        if check():
            cnt += 1

        # 2. return
        return

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            temp.append(i)
            getResult()
            temp.pop()
            visited[i] = False

import sys
sys.stdin = open("sample_input.txt", "r")

# 입력
t = int(input())
for tc in range(t):

    # 입력
    n = int(input())

    # 계산: 백트래킹
    cnt = 0
    arr = [i for i in range(n)]
    visited = [False for _ in range(n)]
    temp = []
    getResult()

    # 출력
    print(f'#{tc+1} {cnt}')