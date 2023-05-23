from collections import deque
import math

def check(x,y,n):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False

def bfs(board, d):

    # 0. bfs 초기 설정
    n = len(board)
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    # 1. bfs
    visited = [[math.inf for _ in range(n)] for _ in range(n)]
    
    queue = deque()
    queue.append((0,0,0,d))
    visited[0][0] = 0
    
    while len(queue) > 0:
        
        cur_x, cur_y, cur_c, cur_d = queue.popleft()
        for next_d in range(4):
            next_x = cur_x + dx[next_d]
            next_y = cur_y + dy[next_d]
            next_c = 0
            if check(next_x, next_y, n) and board[next_x][next_y] == 0:
                
                # 1.
                if cur_d != next_d:
                    next_c = cur_c + 600
                else:
                    next_c = cur_c + 100
                
                # 2.
                if next_c < visited[next_x][next_y]:
                    queue.append((next_x, next_y, next_c, next_d))
                    visited[next_x][next_y] = next_c
    
    return visited[n-1][n-1]

def solution(board):
    
    # 계산1: bfs 오른쪽 시작
    min_right = bfs(board, 0)
    
    # 계산2: bfs 아래쪽 시작
    min_down = bfs(board, 1)
                            
    return min(min_right, min_down)