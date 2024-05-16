import sys
sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(t):

    # 입력
    n, m = map(int,input().split())

    # 계산
    a = 2 * m - n
    b = n - m

    # 출력
    print(f'#{tc + 1} {a} {b}')