import sys
sys.stdin = open('sample_input.txt', 'r')

t = int(input())
for tc in range(t):

    # 입력
    n, d, g = map(int,input().split())

    # 계산
    if d != 0 and g == 0:
        print(f'#{tc+1} Broken')

    elif d != 100 and g == 100:
        print(f'#{tc+1} Broken')

    else:
        isBreak = False
        for match in range(1, n + 1):
            if match * d / 100  == int(match * d / 100):
                isBreak = True
                break

        # 출력
        if isBreak:
            print(f'#{tc+1} Possible')
        else:
            print(f'#{tc+1} Broken')