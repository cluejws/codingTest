def getPrime(max_num):

    prime = []
    visited = [False for _ in range(max_num+1)]

    # 1. 방문처리
    for i in range(2, int(max_num ** 1/2) + 1):

        if visited[i] == False:
            j = 2
            while i * j <= max_num:
                visited[i * j] = True
                j += 1

    # 2. 방문처리 통한 소수
    for i in range(2, max_num + 1):
        if visited[i] == False:
            prime.append(i)

    return prime

import sys
sys.stdin = open("1_input.txt", "r")

# 계산0: 소수 얻기
primes = getPrime(int((10 ** 7) ** 0.5))

# 입력
answer_list = []
t = int(input())
for tc in range(t):

    # 입력
    n = int(input())

    # 계산1: 소인수 분해
    res = 1
    temp = n
    for prime in primes:
        # 1-1: 소수 판단
        cnt = 0
        while temp % prime == 0:
            temp = temp // prime
            cnt += 1

        # 1-2: 소수 반영
        if cnt % 2 != 0:
            res *= prime

    # 계산2
    # temp != 1 -> 최대 소수(3137)보다 작은 소수로 커버X
    # temp == 1 -> 최대 소수(3137)보다 작은 소수로 커버O
    if temp != 1:
        res *= temp

    # 계산3: 출력 계산
    answer_list.append(f'#{tc+1} {res}')

# 출력
for ans in answer_list:
    print(ans)