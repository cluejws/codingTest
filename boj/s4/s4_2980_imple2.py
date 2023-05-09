# 입력
import sys
input = sys.stdin.readline

n, l = map(int,input().split())
list_light = [list(map(int,input().split())) for _ in range(n)]

# 계산1: 시간, 신호등 반영
time = 0
pre_d = 0
for i in range(n):
    d, r, g = list_light[i]

    # 1-1. 위치이동(시간)
    time += (d - pre_d)
    
    # 1-2. 기다림(시간)
    k = time % (r+g)
    if k <= r:
        time += (r - k)

    # 1-3. (신호등)
    pre_d = d

# 계산2: 끝까지 반영
time += (l - pre_d)

# 출력
print(time)