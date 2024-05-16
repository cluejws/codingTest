import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(t):

    # 입력
    n = int(input())
    arr = [list(map(int,list(input()))) for _ in range(n)]

    # 계산0: 초기값
    mid = n // 2
    s = 0

    # 계산1: 위 , 아래
    for i in range(mid):
        for j in range((mid-i), (mid+i) + 1):
            s += arr[i][j]

    for i in range(n-1, mid, -1):
        for j in range((mid-(n-1-i)),(mid+(n-1-i)) + 1):
            s += arr[i][j]

    # 계산2: 중간
    s += sum(arr[mid])

    # 출력
    print(f'#{tc + 1} {s}')