# 입력
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [-1] + list(map(int,input().split()))

# 계산: 누적합
prefix_sum = [0 for _ in range(n+1)]

# 계산1: 누적합 배열 초기화
prefix_sum[0] = 0
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

# 출력
for _ in range(m):
    
    i,j = map(int,input().split())
    print(prefix_sum[j] - prefix_sum[i-1])