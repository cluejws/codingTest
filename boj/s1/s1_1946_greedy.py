# 입력
import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):

    n = int(input())
    list_score = [list(map(int,input().split())) for _ in range(n)]

    # 계산1: 정렬
    list_score.sort(key=lambda x: (x[0], x[1]))

    # 계산2: score 순회 -> 최대값(n)
    cnt = 0
    preScore = math.inf
    for score in list_score:
        a, b = score
        if preScore > b:
            preScore = b
            cnt += 1

    # 출력
    print(cnt)