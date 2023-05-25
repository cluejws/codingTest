# 입력
import sys
input = sys.stdin.readline

n = int(input())
list_ball = list(map(int,input().split()))

# 계산1: 해쉬 판단
dict_ball = {}
for i in range(n):
    
    ball = list_ball[i]
    
    # 1. ball 판단
    if ball in dict_ball:
        dict_ball[ball] += 1
    else:
        dict_ball[ball] = 1
    
    # 2. ball 교체 판단
    if (ball+1) in dict_ball:
        if dict_ball[ball+1] == 1:
            del dict_ball[ball+1]
        else:
            dict_ball[ball+1] -= 1

# 출력
cnt = 0
for ball in dict_ball:
    ballCnt = dict_ball[ball]
    cnt += ballCnt
print(cnt)