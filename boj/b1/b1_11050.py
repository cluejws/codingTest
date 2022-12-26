import sys
input = sys.stdin.readline

n , k = map(int,input().split())

cnt = 1
n_cnt = n
k_cnt = k
up_res = 1
down_res = 1
while cnt <= k:
    up_res *= n_cnt 
    down_res *= k_cnt 
    cnt += 1
    k_cnt -= 1
    n_cnt -= 1

print(up_res//down_res) 