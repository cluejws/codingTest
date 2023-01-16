def getResult(start_x, end_x, start_y, end_y):
    
    
    # 기저조건1: 한칸일 때 끝 
    if (start_x + 1) == end_x and (start_y + 1) == end_y:
        if graph[start_x][start_y] == 0:
            return (1,0)
        elif graph[start_x][start_y] == 1:
            return (0,1)
    
    
    # 기저조건2: 다 같은경우 끝    
    isCheck, color = colorCheck(start_x, end_x, start_y, end_y)
    if isCheck == True:
        if color == 0:
            return (1,0)
        elif color == 1:
            return (0,1)

        
    white_1, blue_1 = getResult(start_x, end_x // 2, end_y // 2, end_y)
    white_2, blue_2 = getResult(start_x, end_x // 2, start_y, end_y // 2)
    white_3, blue_3 = getResult(end_x // 2, end_x, start_y, end_y // 2)
    white_4, blue_4 = getResult(end_x // 2, end_x, end_y // 2, end_y)
    
    sum_white = white_1 + white_2 + white_3 + white_4
    sum_blue = blue_1 + blue_2 + blue_3 + blue_4
    return (sum_white, sum_blue)
        
def colorCheck(start_x, end_x, start_y, end_y):
    
    value = graph[start_x][start_y]
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            if graph[i][j] != value:
                return (False, value)
    
    return (True, value)
            

import sys
sys.setrecursionlimit(10**5)

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
    
# 계산1: 초기화(자르기)
sum_white, sum_blue = getResult(0, n, 0, n)

# 출력
print(sum_white, sum_blue, end='\n')