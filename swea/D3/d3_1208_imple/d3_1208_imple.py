import sys
sys.stdin = open("input.txt", "r")

# 입력
for tc in range(10):

    # 입력
    n = int(input())
    arr = list(map(int,input().split()))

    # 계산: 평탄화
    cnt = -1
    for _ in range(n):

        # 1: 정렬
        arr.sort()

        # 2: 기저 조건
        temp = arr[-1] - arr[0]
        if temp == 0 or temp == 1:
            cnt = temp
            break

        # 3: 평탄화
        arr[-1] -= 1
        arr[0] += 1

        # 4: 결과
        cnt = max(arr) - min(arr)

    # 출력
    print(f'#{tc+1} {cnt}')