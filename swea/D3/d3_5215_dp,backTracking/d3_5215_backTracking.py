def sum_score():

    score = 0
    for i in range(len(temp)):
        score += temp[i][0]

    return score

def sum_calorie():

    calorie = 0
    for i in range(len(temp)):
        calorie += temp[i][1]

    return calorie

def getResult(idx):

    # 기저조건
    global max_score
    max_score = max(max_score, sum_score())

    # 백트래킹
    for i in range(idx, n):
        score, calorie = foods[i]
        if sum_calorie() + calorie <= l:
            temp.append((score, calorie))
            getResult(i+1)
            temp.pop()

import sys
sys.stdin = open("sample_input.txt", "r")

# 입력
t = int(input())
for tc in range(t):

    # 입력
    n, l = map(int,input().split())
    foods = [list(map(int,input().split())) for _ in range(n)]

    # 계산: 백트래킹
    max_score = 0
    temp = []
    getResult(0)

    # 출력
    print(f'#{tc+1} {max_score}')