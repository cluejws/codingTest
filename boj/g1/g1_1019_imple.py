def setNine(n):

    while n % 10 != 9:
        for i in str(n):
            result[int(i)] += cnt
        
        n -= 1
    
    return n

# 입력
import sys
input = sys.stdin.readline

n = int(input())
result = [0 for _ in range(10)]

cnt = 1
while n > 0:

    # 1. (일의 자리)를 9로 만들기
    # -> result 반영
    n = setNine(n)
    
    # 2. (일의 자리+1) * (현재 판단 자릿수)
    # -> result 반영
    if n < 10:
        for i in range(n+1):
            result[i] += cnt

    else:
        for i in range(10):
            result[i] += (n // 10 + 1) * cnt

    # 3.
    # -> 0은 1개 없이 시작
    # -> 다음 판단 자릿수 이동
    # -> 다음 자리 이동
    result[0] -= cnt
    cnt *= 10
    n //= 10

# 출력
print(*result)