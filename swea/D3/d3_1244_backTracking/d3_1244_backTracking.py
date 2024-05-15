def dfs(cnt):

    # 1. 기저조건
    global res
    if cnt == k:
        num = int("".join(map(str, arr)))
        res = max(res, num)
        return

    # 2. dfs
    for x in range(len(arr)-1):
        for y in range(x+1, len(arr)):

            # 2.1
            arr[x], arr[y] = arr[y], arr[x]

            # 2.2: 겹치는 경우 제외
            num = int("".join(map(str, arr)))
            if (cnt, num) not in temp:
                dfs(cnt + 1)
                temp.append((cnt, num))

            # 2.3
            arr[x], arr[y] = arr[y], arr[x]

import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(t):

    # 입력
    n, k = input().split()

    # 계산1: 변화
    arr = list(n)
    k = int(k)

    # 계산2: dfs
    res = 0
    temp = []
    dfs(0)

    # 출력
    print(f'#{tc+1} {res}')