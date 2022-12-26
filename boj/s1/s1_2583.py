def check(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

def get_cnt(x,y):

    # bfs 및 개수세기
    cnt = 0

    queue = deque()

    queue.append((x,y))
    cnt += 1
    visited[x][y] = True

    while len(queue) != 0:
        cur_x, cur_y = queue.popleft()

        for k in range(4):
            next_x = cur_x + dx[k]
            next_y = cur_y + dy[k]

            if check(next_x,next_y) and graph[next_x][next_y] == 0:
                if visited[next_x][next_y] == False:
                    visited[next_x][next_y] = True
                    queue.append((next_x,next_y))
                    cnt += 1
    return cnt

# 입력1: 그래프
from collections import deque

n, m, k = map(int,input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
graph = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

# 입력2: 방문처리
for _ in range(k):
    a,b,c,d = map(int,input().split())
    for i in range(n-d, n-b):
        for j in range(a, c):
            graph[i][j] = 1

# 계산1: bfs 통한 개수 세기
cnt_arr = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == False:
            cnt = get_cnt(i,j)
            cnt_arr.append(cnt)

# 계산2: 출력 정렬
cnt_arr.sort()

# 출력
print(len(cnt_arr))
print(" ".join(list(map(str,cnt_arr))))
