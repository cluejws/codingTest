# 입력
from collections import deque

import sys
input = sys.stdin.readline

n = int(input())
list_value = list(map(int,input().split()))

# 계산1: 정렬
list_value.sort()

# 계산2: 가장 작은 것, 가장 큰 것
# 1.
max_res = 0
queue = deque(list_value)
while len(queue) >= 2:
    front = queue.popleft()
    back = queue.pop()

    max_res += (back * 2)

# 2.
if len(queue) == 1:
    max_res += queue[0]

# 출력
print(max_res)