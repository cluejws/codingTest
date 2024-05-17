import sys
sys.stdin = open("sample_input.txt", "r")

test_case = int(input())
for tc in range(test_case):

    # 입력
    n, t, p = map(int,input().split())
    humans = [list(map(int,input().split())) for _ in range(n)]

    # 계산1: 문제 점수 얻기
    scores = [0 for _ in range(t)]
    for human in humans:

        for i in range(t):
            if human[i] == 0:
                scores[i] += 1

    # 계산2: 사람 푼 문제 수 / 사람 점수 얻기
    human_problems = [sum(humans[idx]) for idx in range(n)]
    human_scores = [0 for _ in range(n)]
    for k in range(n):
        for i in range(t):
            if humans[k][i] == 1:
                human_scores[k] += (scores[i])

    # 계산3: 사람 등수 얻기
    human_infos = [[human_scores[idx], human_problems[idx], idx] for idx in range(n)]

    # 1: 자신보다 많은 점수를 획득
    # 2: 자신과 같은 점수를 획득 / 더 많은 문제를 품
    # 3: 자신과 같은 점수를 획득 / 같은 수의 문제를 품 / 번호가 더 작음
    human_infos.sort(key = lambda x: (-x[0], -x[1], x[2]))

    # 출력
    for rank, info in enumerate(human_infos):
        score, problem, idx = info
        if idx == (p - 1):
            print(f'#{tc + 1} {score} {rank + 1}')