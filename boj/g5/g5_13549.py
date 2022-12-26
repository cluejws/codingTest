def check(x):
    if 0<=x<=100000:
        return True
    else:
        return False

# 입력
from collections import deque

n, k = map(int,input().split())
visited = [-1 for _ in range(100001)]

# 계산(bfs)
queue = deque()
queue.append(n)
visited[n] = 0

while len(queue) != 0:

    pos = queue.popleft()
    if pos == k:
        print(visited[k])
        quit()

    double_pos = pos * 2
    minus_pos = pos - 1
    plus_pos = pos + 1

    if check(double_pos):
        if visited[double_pos] == -1:
            queue.append(double_pos)
            visited[double_pos] = visited[pos]

    if check(minus_pos):
        if visited[minus_pos] == -1:
            queue.append(minus_pos)
            visited[minus_pos] = visited[pos] + 1
        else:
            visited[minus_pos] = min(visited[pos]+1, visited[minus_pos])

    if check(plus_pos):
        if visited[plus_pos] == -1:
            queue.append(plus_pos)
            visited[plus_pos] = visited[pos] + 1
        else:
            visited[plus_pos] = min(visited[pos]+1, visited[plus_pos])