def getPrime(n):
    
    visited = [True for _ in range(n+1)]

    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(n ** 0.5)+1):
        if visited[i] == True:
            j = 2
            while i * j <= n:
                visited[i * j] = False
                j += 1

    prime = []
    for i in range(2, n+1):
        if visited[i] == True:
            prime.append(i)

    return prime

# 입력
import sys
input = sys.stdin.readline

n = int(input())

# 계산0: 숫자1 -> 예외처리
if n == 1:
    print(0)
    quit()

# 계산1: 소수 얻기
prime = getPrime(n)
k = len(prime)

# 계산2: 투포인터
cnt = 0

j = 0
sum_res = prime[j]
for i in range(k):

    # 1.
    while j + 1 < k and sum_res < n:
        sum_res += prime[j + 1]
        j += 1

    # 2.
    if sum_res < n:
        break

    # 3.
    if sum_res == n:
        cnt += 1

    # 4.
    sum_res -= prime[i] 

# 출력
print(cnt)