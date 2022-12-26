import sys
input = sys.stdin.readline

def getResult(n):
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,n)
# 입력
import heapq
n = int(input())

heap = []
for _ in range(n):
    num = int(input())
    getResult(num)