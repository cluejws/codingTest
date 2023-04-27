# 입력
import sys
input = sys.stdin.readline

n, c = map(int,input().split())
m = int(input())
list_line = [tuple(map(int,input().split())) for _ in range(m)]

# 계산1: 정렬(end, start)
list_line.sort(key=lambda x: (x[1], x[0]))

# 계산2: 그리디(배송(-) -> 싣기(+))
cnt = 0
boxes = [0 for _ in range(n+1)]
for line in list_line:
    start, end, box = line
    
    # 1. start부터 end 도착 전 까지 박스를 최대로 싣기 판단
    # -> "최소 값 까지만 실는 것"이 "최대로 실는 것"
    # -> (1) box만큼 추가, (2) 최대 양 - 기존에 실었던 양
    maxbox = box
    for i in range(start, end):
        maxbox = min(maxbox, c - boxes[i])

    # 2. start부터 end 도착 전 까지 박스를 최대로 싣기 반영
    for i in range(start, end):
        boxes[i] += maxbox
    
    # 3. end 에서 최대로 배송
    cnt += maxbox

# 출력
print(cnt)