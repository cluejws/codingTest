import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(t):

    # 입력
    n, m, k = map(int,input().split())
    times = list(map(int,input().split()))
    times.sort()

    # 계산: left 비교
    # (times[i] // m) * k : 해당 시점에 생성된 빵 개수
    # (i + 1) : 해당 시점까지 사람 수
    isBreak = False
    for i in range(n):
        left = (times[i] // m ) * k - (i + 1)
        if left < 0:
            print(f'#{tc + 1} Impossible')
            isBreak = True
            break

    if not isBreak:
        print(f'#{tc + 1} Possible')