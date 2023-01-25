def getMove(x):
    
    while isLadder(x)[0] or isSnake(x)[0]:

        flag, value = isLadder(x)
        if flag:
            x = value
            continue
        
        flag, value = isSnake(x)
        if flag:
            x = value
            continue
        
    return x
        
def isLadder(x):
    
    for ladder in ladders:
        if x == ladder[0]:
            return (True, ladder[1])

    return (False, -1)

def isSnake(x):
    
    for snake in snakes:
        if x == snake[0]:
            return (True, snake[1])
    
    return (False, -1)

def check(x):
    if x > 100:
        return False
    else:
        return True
        
def getResult():
    visited = [-1 for _ in range(100+1)]
    queue = deque()
    queue.append(1)
    visited[1] = 0

    while len(queue) != 0:

        cur_point = queue.popleft()
        if cur_point == 100:
            return visited[cur_point]

        
        for i in range(6):
            
            next_point = cur_point + square[i]
            
            # 계산: 최대한 움직이기
            move_point = getMove(next_point)
            if check(move_point) and visited[move_point] == -1:
                queue.append(move_point)
                visited[move_point] = visited[cur_point] + 1

# 입력  
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
ladders = [list(map(int,input().split())) for _ in range(n)]
ladders.sort(key= lambda x: (x[0]))

snakes = [list(map(int,input().split())) for _ in range(m)]
snakes.sort(key= lambda x: (-x[0]))

square = [1,2,3,4,5,6]

# 계산: bfs
min_res = getResult()

# 출력
print(min_res)