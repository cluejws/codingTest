# 입력
import sys, heapq
input = sys.stdin.readline

n = int(input())
list_card = [int(input()) for _ in range(n)]

# 계산1: 우선순위 큐 생성 
heap = []
for card in list_card:
    heapq.heappush(heap, card)

# 계산2: 가장 작은 2개 제거
min_res = 0
while len(heap) >= 2:
    data1 = heapq.heappop(heap)
    data2 = heapq.heappop(heap)
    heapq.heappush(heap, (data1+data2))

    min_res += (data1+data2)

# 출력
print(min_res)