import sys
sys.stdin = open("sample_input.txt", "r")

# 입력
for tc in range(10):

    # 입력
    n = int(input())
    apt_list = list(map(int,input().split()))

    # 계산
    cnt = 0
    for i in range(2, n-2):
        apt = apt_list[i]
        max_apt = max(apt_list[i-2], apt_list[i-1], apt_list[i+1], apt_list[i+2])

        if max_apt < apt:
            cnt += (apt - max_apt)

    # 출력
    print(f'#{tc+1} {cnt}')