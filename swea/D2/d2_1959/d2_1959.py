import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(t):

    # 1. 입력
    n, m = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))

    # 2. 계산
    max_value = 0
    if n <= m:
        for i in range(m - n + 1):
            # 2.1: 합
            s = 0
            for k in range(n):
                s += (arr1[k] * arr2[i + k])

            # 2.2: 최대값
            max_value = max(s, max_value)
    else:
        for i in range(n - m + 1):

            # 2.1: 합
            s = 0
            for k in range(m):
                s += (arr2[k] * arr1[i + k])

            # 2.2: 최대값
            max_value = max(s, max_value)

    print(f'#{tc+1} {max_value}')