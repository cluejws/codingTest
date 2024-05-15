import sys
sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(t):

    # 입력
    n = int(input())

    # 2: 계산
    arr = []
    temp = 0
    while len(arr) < 10:

        # 2.1: 배수
        temp += n

        # 2-2: 문자열 반영
        for s in str(temp):
            if s not in arr:
                arr.append(s)

    print(f'#{tc+1} {temp}')
