def dfs(start):

    # 1. 기저조건
    global cnt
    if sum(temp) > k:
        return
    elif sum(temp) == k:
        cnt += 1
        return

    # 2. dfs
    for i in range(start, n):
            temp.append(arr[i])
            dfs(i+1)
            temp.pop()

import sys
sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(t):

    # 입력
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))

    # 계산: dfs
    cnt = 0
    temp = []
    dfs(0)

    # 출력
    print(f'#{tc + 1} {cnt}')