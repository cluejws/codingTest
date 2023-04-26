# 입력
import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    list_num = list(map(int,input().split()))
    
    # 계산1: 우선순위 큐 초기화
    heap = []
    for num in list_num:
        heapq.heappush(heap, num)

    # 계산2: 1개 남을때 까지 진행
    min_res = 0
    while len(heap) >= 2:
        data1 = heapq.heappop(heap)
        data2 = heapq.heappop(heap)
        heapq.heappush(heap, (data1 + data2))
        min_res += (data1 + data2) 
        
    # 출력
    print(min_res)