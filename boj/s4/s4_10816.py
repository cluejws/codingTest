import sys
input = sys.stdin.readline

n = int(input())
n_arr = list(map(int,input().split()))

k = int(input())
k_arr = list(map(int,input().split()))
k_dict = {}


for ka in k_arr:
    if ka not in k_dict:
        k_dict[ka] = 0
        
for na in n_arr:
    if na in k_dict:
        k_dict[na] += 1

# 출력
for ka in k_arr:
    print(k_dict[ka], end =" ")