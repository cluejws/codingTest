import sys
sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(t):

    # 입력
    p = input().strip()
    q = input().strip()

    # 출력
    if p + 'a' != q:
        print(f'#{tc + 1} Y')
    else:
        print(f'#{tc + 1} N')
