# 입력
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
list_start = [input().rstrip() for _ in range(n)]
list_end = [input().rstrip() for _ in range(n)]

# 계산1: end 덱 화
deque_end = deque(list_end)

# 계산2: end, start 제거하면서 판단
cnt = 0
while len(deque_end) > 0:

    # 1.
    data = deque_end.popleft()
    
    # 2.
    if list_start[0] != data:
        cnt += 1
    
    # 3.
    list_start.remove(data)

# 출력
print(cnt)   