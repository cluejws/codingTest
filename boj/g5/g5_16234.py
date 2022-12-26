def set_avg(arr, sum):
    
    # 계산1: 평균 구하기
    res = sum // len(arr)
    
    # 계산2: graph변화
    for a in arr:
        x,y = a
        graph[x][y] = res
    
def check_move(cur_x, cur_y, temp_x,temp_y):
    
    res = abs(graph[cur_x][cur_y] - graph[temp_x][temp_y])
    
    if l<=res<=r:
        return True
    else:
        return False
    
def check(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else: 
        return False

def bfs(x,y, visit):
    
    arr = []
    sum = 0
    
    arr.append((x,y))
    sum += graph[x][y]
    
    queue = deque()
    queue.append((x,y))
    visited[x][y] = visit
    
    while len(queue) != 0:
        
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            
            temp_x = cur_x + dx[i]
            temp_y = cur_y + dy[i]
            
            if check(temp_x,temp_y):
                if check_move(cur_x, cur_y, temp_x, temp_y) and visited[temp_x][temp_y] == -1:
                    
                    queue.append((temp_x,temp_y))
                    visited[temp_x][temp_y] = visit
                    
                    arr.append((temp_x,temp_y))
                    sum += graph[temp_x][temp_y]
    
    return (arr, sum)

from collections import deque
 
n,l,r = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

cnt = 0
while True:
    
    is_cnt = False
    visit = 0
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                
                # 계산1: visited를 통해 모두 한번씩 방문해서 그룹만들기
                arr, sum = bfs(i,j, visit)
                if len(arr) > 1:
                    
                    # 계산2: 그룹끼리 graph 평균으로 변화
                    set_avg(arr,sum)
                    
                    is_cnt = True
                                    
                # 계산3: 그룹번호 증가
                visit += 1
    
    if is_cnt:
        cnt += 1
    else:
        break
print(cnt)