# 입력
import sys, heapq
input = sys.stdin.readline

n = int(input())
list_room = [tuple(map(int,input().split())) for _ in range(n)]

# 계산1: 정렬
list_room.sort(key=lambda x: (x[0], x[1]))

# 계산2: 최소 강의실 개수
# 우선순위 큐를 통해 
# -> 가장 작은 끝 <= 다음 시작: 새로 추가 X
# -> 가장 작은 끝 > 다음 시작: 새로 추가
heap = []
heapq.heappush(heap, list_room[0][1])
for i in range(1, n):

    start, end = list_room[i]
    if heap[0] > start:
        heapq.heappush(heap, end)
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, end)

# 출력
print(len(heap))