# 입력
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

# 계산1: 분자
res = 1
for _ in range(m):
    res *= n
    n -= 1
    
# 계산2: 분모
for i in range(m, 0, -1):
    res //= i

# 출력
print(res)