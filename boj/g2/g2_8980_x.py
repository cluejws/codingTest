# 입력
import sys, heapq
input = sys.stdin.readline

n, c = map(int,input().split())
m = int(input())
list_line = [tuple(map(int,input().split())) for _ in range(m)]

# 계산1: 우선순위큐 생성
end_heap = []
for line in list_line:
    start, end, box = line
    heapq.heappush(end_heap, (end, box))

start_heap = []
for line in list_line:
    start, end, box = line
    heapq.heappush(start_heap, (start, box))

# 계산2: 마을 번호 순회
# 그리디(배송(-) -> 싣기(+))
cnt = 0
carry = 0
for i in range(1, n+1):
    
    # 1. 마을 i위치에서 배송
    while len(end_heap) > 0 and end_heap[0][0] == i:
        end, box = heapq.heappop(end_heap)
        if carry >= box:
            cnt += box
            carry -= box
        else:
            cnt += carry
            carry = 0        

    # 2. 마을 i위치에서 싣기
    while len(start_heap) > 0 and start_heap[0][0] == i:
        start, box = heapq.heappop(start_heap)
        if start == i:
            if (carry + box) <= c:
                carry += box
            else:
                carry = c

# 출력
print(cnt)