def getResult(x):

    # 1. 기저조건
    global max_res
    max_res = max(max_res, len(temp))

    # 2. 백트래킹
    for y in graph[x]:
        if visited[y] == False:
            visited[y] = True
            temp.append(y)
            getResult(y)
            temp.pop()
            visited[y] = False

import sys
sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(t):

    # 입력
    n, m = map(int,input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        x, y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)

    # 계산
    max_res = 0
    visited = [False for _ in range(n+1)]
    temp = []
    for i in range(1, n + 1):
        visited[i] = True
        temp.append(i)
        getResult(i)
        temp.pop()
        visited[i] = False

    # 출력
    print(f'#{tc + 1} {max_res}')