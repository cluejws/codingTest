# 입력
import sys, heapq
input = sys.stdin.readline

n = int(input())
list_room = [list(map(int,input().split())) for _ in range(n)]

# 계산1: 정렬(시작 시간)
list_room.sort(key=lambda x: (x[1]))

# 계산2: 최소 힙
min_heap = []
for room in list_room:
    num, start, end = room
    if len(min_heap) > 0 and min_heap[0] <= start:
        data = heapq.heappop(min_heap)

    heapq.heappush(min_heap, end)

# 출력
print(len(min_heap))