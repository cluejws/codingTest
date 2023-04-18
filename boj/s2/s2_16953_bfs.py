def check(x):
    if 1<=x<=b:
        return True
    else:
        return False

def bfs(a):
    dict_point = {}
    queue = deque()

    queue.append(a)
    dict_point[a] = 1

    while len(queue) != 0:

        cur_point = queue.popleft()
        if cur_point == b:
            return dict_point[cur_point]

        next_point = cur_point * 2
        if check(next_point):
            if next_point not in dict_point:
                queue.append(next_point)
                dict_point[next_point] = dict_point[cur_point] + 1

        next_point = int(str(cur_point) + '1')
        if check(next_point):
            if next_point not in dict_point:
                queue.append(next_point)
                dict_point[next_point] = dict_point[cur_point] + 1

    return -1
    
# 입력
from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int,input().split())

# 계산 및 출력: bfs
print(bfs(a))