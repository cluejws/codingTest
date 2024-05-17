import sys
sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(t):

    # 입력
    dict_answer = {}
    n = int(input())
    for _ in range(n):
        # 1: 입력
        a, b, c, d, s = input().split()
        a, b, c, d = int(a), int(b), int(c), int(d)

        # 2: 반영
        if s == 'YES':
            dict_answer[a] = True
            dict_answer[b] = True
            dict_answer[c] = True
            dict_answer[d] = True

        elif s == 'NO':
            dict_answer[a] = False
            dict_answer[b] = False
            dict_answer[c] = False
            dict_answer[d] = False

    # 출력
    for answer in dict_answer:
        if dict_answer[answer]:
            print(f'#{tc + 1} {answer}')
            continue