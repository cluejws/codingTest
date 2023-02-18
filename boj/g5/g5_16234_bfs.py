def checkRange(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False

def checkMove(x1,y1, x2, y2):
    
    res = graph[x1][y1] - graph[x2][y2]
    if l<= abs(res)<= r:
        return True
    else:
        return False

def bfs(x,y):
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    arr = []
    
    queue = deque()
    visited[x][y] = True
    queue.append((x,y))
    arr.append((x,y))
    
    while len(queue) != 0:
        
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            
            if checkRange(next_x, next_y):
                if checkMove(cur_x,cur_y,next_x,next_y) and visited[next_x][next_y] == False:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))
                    arr.append((next_x,next_y))
    
    arr_sum = 0
    for ax, ay in arr:
        arr_sum += graph[ax][ay]
    
    return arr, arr_sum
    

from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
while True:
    
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    # 계산1: bfs
    is_group_cnt = False
    for i in range(n):
        for j in range(n):
            
            
            if visited[i][j] == False:
            
                # 계산1-1: 그룹, 그룹 합
                arr, arr_sum = bfs(i,j)
            
                # 계산1-2: 
                if len(arr) > 1:
                    # (1) 평균으로 할당(방문처리했기 때문에 그냥 바로 적용 가능)
                    arr_avg = arr_sum // len(arr)
                    for ax, ay in arr:
                        graph[ax][ay] = arr_avg
                        
                    # (2) 인구이동 시 개수 세기 flag 변경
                    is_group_cnt = True

    # 계산2: 다음 인구이동 여부 판단
    if is_group_cnt == True:
        cnt += 1
    else:
        break

    #print('----')
    
print(cnt)