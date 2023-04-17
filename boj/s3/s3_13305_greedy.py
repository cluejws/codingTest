# 입력
import sys, math
input = sys.stdin.readline

n = int(input())
list_dist = list(map(int,input().split()))
list_place = list(map(int,input().split()))

# 계산: 그리디
min_cnt = 0
min_place = math.inf
for i in range(n-1):
    
    # 1. 거리
    dist = list_dist[i]
    
    # 2. 최소 주유
    min_place = min(min_place, list_place[i])

    # 3. 계산
    min_cnt += dist * min_place

# 출력
print(min_cnt)