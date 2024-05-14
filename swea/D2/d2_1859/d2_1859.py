import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(t):

    # 입력
    n = int(input())
    arr = list(map(int,input().split()))

    # 계산
    s = 0
    max_price = arr[-1]
    for i in range(n-2, -1, -1):
        if arr[i] <= max_price:
            s += (max_price - arr[i])
        else:
            max_price = arr[i]

    print(f'#{tc+1} {s}')