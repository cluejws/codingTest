# 입력
import sys, math
input = sys.stdin.readline

input_alp = input().rstrip()

# 계산1: a 개수 세기
aCount = 0
for alp in input_alp:
    if alp == 'a':
        aCount += 1

# 계산2: 슬라이딩 윈도우 범위 늘리기
# 윈도우 크기(aCount)
extend_alp = input_alp + input_alp[:aCount-1]

# 계산2: 슬라이딩 윈도우
# 윈도우 크기(aCount)
min_cnt = math.inf

n = len(input_alp)
for i in range(n):
    cnt = 0
    for alp in extend_alp[i:i+aCount]:
        if alp == 'b':
            cnt += 1
    
    min_cnt = min(min_cnt, cnt)

# 출력
print(min_cnt)