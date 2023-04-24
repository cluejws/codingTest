# 입력
import sys
input = sys.stdin.readline

n = int(input())
list_pos = list(map(int,input().split()))

# 계산1: 누적합
prefix_sum = [0 for _ in range(n)]
prefix_sum[0] = list_pos[0]
for i in range(1, n):
    pos = list_pos[i]
    prefix_sum[i] = prefix_sum[i-1] + pos

# 계산2: 경우 3개
max_res = 0

# 1. 벌 (벌) 꿀
for i in range(1, n-1):
    sum_res = 2 * prefix_sum[-1]
    
    # 벌1
    sum_res -= list_pos[0]
    sum_res -= list_pos[i]

    # 벌2
    sum_res -= prefix_sum[i]
    
    max_res = max(max_res, sum_res)

# 2. 벌 (꿀) 벌
for i in range(1, n-1):
    
    # 벌1
    sum_res = prefix_sum[i]
    sum_res -= list_pos[0]

    # 벌2
    sum_res += (prefix_sum[-1] - prefix_sum[i-1])
    sum_res -= list_pos[-1]

    max_res = max(max_res, sum_res)

# 3. 꿀 (벌) 벌
for i in range(1, n-1):
    
    # 벌2
    sum_res = prefix_sum[-1]
    sum_res -= list_pos[-1]
    sum_res -= list_pos[i]

    # 벌1
    sum_res += (prefix_sum[i-1])

    max_res = max(max_res, sum_res)

# 출력
print(max_res)