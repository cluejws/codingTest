def check(x,y):
    if 0<=x<r and 0<=y<c:
        return True
    else:
        return False

# 계산4: 클러스터 움직이기
def moveCluster(r,c, cluster):
    
    # 계산:
    # 정렬해서 가장 아래쪽에 있는 것만 판단
    cluster.sort(key = lambda x: (x[0],x[1]), reverse = True)
    change = [100 for _ in range(100)]

    # 계산1: 각 열에서 밑바닥(땅 또는 미네랄)과 최소 차이 찾기
    # cluster에서 pos 꺼내기 / 방문한 열은 이미 밑바닥에서 최소 차이
    for pos in cluster:
        x, y = pos
        
        if change[y] == 100:
            for i in range(r-1, x, -1):
                if graph[i][y] == 'x':
                    change[y] = (i-1) - x
            
            if change[y] == 100:
                change[y] = (r-1) - x

    # 계산2: 열끼리 밑바닥(땅 또는 미네랄)과 최소 차이 찾기
    min_change = min(change)
    
    # 계산3: 그래프 변화
    for pos in cluster:
        x,y = pos
        graph[x][y] = '.'
        graph[x+min_change][y] = 'x'

# 계산3: 클러스터 얻기 
def getClusters(r, c, bar_x, bar_y):
    
    clusters = []
    visited = [[False for _ in range(c)] for _ in range(r)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    # 계산
    # 상하좌우로 bfs 
    # -> cluster에 계속 담기 
    # -> 만약 밑바닥과 붙어있으면 cluster를 clusters에 담기 X
    for i in range(4):
        cluster = []
        isBottomCluster = False
        
        # 계산1: 시작점이 범위에 포함? / 방문하지 않은 곳? / 미네랄인 곳?
        start_x = bar_x + dx[i]
        start_y = bar_y + dy[i]
        if check(start_x, start_y) and visited[start_x][start_y] == False and graph[start_x][start_y] == 'x':
                
                # 계산2: 시작점 부터 BFS
                cluster.append((start_x,start_y))
                queue = deque()
                queue.append((start_x,start_y))
                visited[start_x][start_y] = True
                
                while len(queue) != 0:
                    
                    cur_x, cur_y = queue.popleft()
                    
                    # 밑바닥과 붙어있으면 cluster를 clusters에 담기 X
                    if cur_x == r-1:
                        isBottomCluster = True
                    
                    for j in range(4):
                        next_x = cur_x + dx[j]
                        next_y = cur_y + dy[j]
                        
                        if check(next_x, next_y) and visited[next_x][next_y] == False and graph[next_x][next_y] == 'x':
                            cluster.append((next_x,next_y))
                            queue.append((next_x,next_y))
                            visited[next_x][next_y] = True
                
                # 계산3: 밑바닥이 아닌 cluster를 clusters에 담기
                if not isBottomCluster:
                    clusters.append(cluster)
    return clusters
            
# 계산1: n 높이로 막대 던져서, 부셔지는 미네랄 위치 얻기         
def getBarPos(x_pos, cnt):
    
    # 왼쪽, 오른쪽
    if cnt % 2 == 0:
        pos_graph = graph[x_pos][:]
        for i in range(len(pos_graph)):
            if pos_graph[i] == 'x':
                return x_pos, i
    else:
        pos_graph = graph[x_pos][:]
        for i in range(len(pos_graph)-1, -1, -1):
            if pos_graph[i] == 'x':
                return x_pos, i

    return (-1, -1) # 미네랄 없어서 그냥 지나감
    
# 입력
from collections import deque

r,c = map(int,input().split())
graph = [list(input()) for _  in range(r)]
num = int(input())
n_arr = list(map(int,input().split()))

# 계산
for i in range(len(n_arr)):
    
    # 계산1: n 높이로 막대 던져서, 부셔지는 미네랄 위치 얻기
    n = n_arr[i] 
    bar_x, bar_y = getBarPos(r-n, i)
    if bar_x == -1 and bar_y == -1:
        continue
    
    # 계산2: 그래프 변형
    graph[bar_x][bar_y] = '.'

    # 계산3: 클러스터 얻기
    clusters = getClusters(r,c,bar_x,bar_y)
    if len(clusters) == 0:
        continue

    # 계산4: 클러스터 움직이기
    for cluster in clusters:
        moveCluster(r,c,cluster)

# 출력
for item in graph:
    print(''.join(item))