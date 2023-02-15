def check(x):
    if 0<=x<=100000:
        return True
    else:
        return False

def bfs(n,k):
    
    queue = deque()
    queue.append(n)
    visited[n] = 0
    
    while len(queue) != 0:
        
        global res_dist, res_cnt
        
        # 현재 점
        cur_point = queue.popleft()
        if cur_point == k:
            res_dist = visited[k]
            res_cnt += 1
        
        # 다음 점
        next_point = cur_point + 1
        if check(next_point):
            if visited[next_point] == -1 or visited[next_point] == visited[cur_point] + 1:
                queue.append(next_point)
                visited[next_point] = visited[cur_point] + 1

        next_point = cur_point - 1
        if check(next_point):
            if visited[next_point] == -1 or visited[next_point] == visited[cur_point] + 1:
                queue.append(next_point)
                visited[next_point] = visited[cur_point] + 1

        next_point = cur_point * 2
        if check(next_point):
            if visited[next_point] == -1 or visited[next_point] == visited[cur_point] + 1:
                queue.append(next_point)
                visited[next_point] = visited[cur_point] + 1

# 입력
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())

visited = [-1 for _ in range(100000+1)]

# 계산: bfs
res_dist = 0
res_cnt = 0
bfs(n,k)

# 출력
print(res_dist)
print(res_cnt)