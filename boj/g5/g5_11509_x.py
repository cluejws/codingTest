# 입력
import sys, heapq
input = sys.stdin.readline

n = int(input())
list_ball = list(map(int,input().split()))

# 계산1: 최대 힙 생성
max_heap = []
for i in range(n):
    ball = list_ball[i]
    heapq.heappush(max_heap, (-ball, i))

# 계산2: 최소 개수
cnt = 0
visited = [False for _ in range(n)]
while len(max_heap) > 0:

    # 1. 최대 제거
    minus_ball, max_index = heapq.heappop(max_heap)
    max_ball = minus_ball * -1
    
    # 2
    # 2.1: 방문 판단
    if visited[max_index] == True:
        continue
    
    # 2.2: 방문 처리 / 개수 세기
    visited[max_index] = True
    cnt += 1

    # 3. 
    # 3.1: 높이 판단
    height = max_ball - 1
    if height == 0:
        continue

    # 3.2: 이후 제거
    for i in range(max_index+1, n):
        if visited[i] == False and list_ball[i] == height:
            visited[i] = True
            height -= 1

# 출력
print(cnt)