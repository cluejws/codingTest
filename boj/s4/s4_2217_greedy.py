# 입력
import sys
input = sys.stdin.readline

n = int(input())
list_line = [int(input()) for _ in range(n)]

# 계산1: 정렬
list_line.sort()

# 계산2: 그리디
max_sum = -1
for i in range(n):
    
    # 1. 최소 길이
    min_line = list_line[i]

    # 2. 최소 길이부터 끝 길이까지 개수
    max_sum = max(max_sum, min_line * (n-i))

# 출력
print(max_sum)