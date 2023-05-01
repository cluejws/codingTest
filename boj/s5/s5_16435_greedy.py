# 입력
import sys
input = sys.stdin.readline

n, l = map(int,input().split())
list_fruit = list(map(int,input().split()))

# 계산1: 정렬
list_fruit.sort()

# 계산2: 그리디
for i in range(n):
    
    # 1. 기저조건
    if l < list_fruit[i]:
        break

    # 2. 먹고 반영
    l += 1

# 출력
print(l)