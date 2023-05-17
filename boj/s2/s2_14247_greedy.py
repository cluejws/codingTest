# 입력
import sys
input = sys.stdin.readline

n = int(input())
list_tree = list(map(int,input().split()))
list_up = list(map(int,input().split()))

# 계산1: 동기화(나무 길이, 성장 속도)
list_info = []
for i in range(n):
    list_info.append((list_tree[i], list_up[i]))

# 계산2: 오름차순 정렬(성장 속도) 
list_info.sort(key= lambda x: (x[1]))

# 계산3: 최대합
max_res = 0
for i in range(n):
    max_res += (list_info[i][0] + list_info[i][1] * i)

# 출력
print(max_res)