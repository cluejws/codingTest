# 입력
import sys
input = sys.stdin.readline

n = int(input())

# 계산1: 5의 최대 제곱수 범위 판단
k = 1
while n // (5**k) > 0: 
    k += 1
k -= 1

# 계산2: 5의 최대 제곱수 범위 내 (5 포함 개수 세기)
cnt = 0
for i in range(1, n+1):
    
    for j in range(k, 0, -1):
        if i % (5**j) == 0:
            # print(f'{i}일때 {j}만큼')
            cnt += j
            break

# 출력
print(cnt)