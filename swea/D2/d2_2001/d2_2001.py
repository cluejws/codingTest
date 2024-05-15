import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(t):

    # 1: 입력
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    # 2: 계산
    max_value = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):

            # 2-1: 합
            temp = 0
            for x in range(i, i+m):
                for y in range(j, j+m):
                    temp += (arr[x][y])

            # 2-2: 최대 비교
            max_value = max(max_value, temp)

    # 3: 출력
    print(f'#{tc+1} {max_value}')