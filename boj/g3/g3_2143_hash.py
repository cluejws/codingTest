# 입력
import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int,input().split()))

m = int(input())
b = list(map(int,input().split()))

# 계산1: 누적합 생성
prefix_sum_a = [0 for _ in range(n)]
prefix_sum_a[0] = a[0]
for i in range(1, n):
    prefix_sum_a[i] = prefix_sum_a[i-1] + a[i]

prefix_sum_b = [0 for _ in range(m)]
prefix_sum_b[0] = b[0]
for i in range(1, m):
    prefix_sum_b[i] = prefix_sum_b[i-1] + b[i]

# 계산2: 딕셔너리 생성
dict_a = {}
for i in range(n):

    for j in range(i, n):
        sum_res = prefix_sum_a[j] - prefix_sum_a[i] + a[i]
        if sum_res in dict_a:
            dict_a[sum_res] += 1
        else:
            dict_a[sum_res] = 1

dict_b = {}
for i in range(m):

    for j in range(i, m):
        sum_res = prefix_sum_b[j] - prefix_sum_b[i] + b[i]
        if sum_res in dict_b:
            dict_b[sum_res] += 1
        else:
            dict_b[sum_res] = 1

# 계산3: 차이 조회
res = 0
for key1 in dict_a:
    diff = t - key1
    if diff in dict_b:
        res += (dict_a[key1] * dict_b[diff])
    
# 출력
print(res)