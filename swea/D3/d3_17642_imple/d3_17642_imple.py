import sys
sys.stdin = open("sample_input.txt", "r")

t = int(input())
for tc in range(t):

    # 입력
    a, b = map(int,input().split())

    # 계산1: 차이
    diff = b-a

    # 계산2: 짝(2의 배수), 홀(2의배수+3) 구분
    cnt = 0
    if diff % 2 == 0:
        cnt += (diff // 2)
    else:
        # 2 개수, 3개수
        cnt += ((diff // 2) - 1)
        cnt += 1

    # 출력
    if diff == 0:
        print(f'#{tc + 1} {0}')
        continue

    if diff <= 1:
        print(f'#{tc + 1} {-1}')
        continue

    print(f'#{tc + 1} {cnt}')