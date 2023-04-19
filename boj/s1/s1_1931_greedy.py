# 입력
import sys
input = sys.stdin.readline

n = int(input())
list_room = [tuple(map(int,input().split())) for _ in range(n)]

# 계산1: 정렬
list_room.sort(key=lambda x: (x[1], x[0]))

# 계산2: 회의 최대 개수
end = 0
cnt = 0
for i in range(n):
    room = list_room[i]
    cur_start, cur_end = room
    if end <= cur_start:
        cnt += 1
        end = cur_end

# 출력
print(cnt)