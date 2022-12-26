# 그래프 == 0 (graph[i][j] = bottom)
# 그래프 != 0 (bottom = graph[i][j], graph[i][j]=0)
# 주사위 이동할때마다 top 출력
# 주사위 바깥 이동x (출력x, 명령x)
def check(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

def east_move(x,y):
    global top, bottom, north, south, east, west
    
    # 범위 체크
    temp_x = x
    temp_y = y+1
    if check(temp_x,temp_y):
        
        #1. 주사위 변형(동쪽)
        temp_bottom = bottom
        bottom = east
        east = top
        top = west
        west = temp_bottom
    
        #2. 주사위 변형 값으로 그래프 변형
        if(graph[temp_x][temp_y] == 0):
            graph[temp_x][temp_y] = bottom
        else:
            bottom = graph[temp_x][temp_y]
            graph[temp_x][temp_y] = 0

        return temp_x, temp_y
    else:
        return x,y

def west_move(x,y):
    global top, bottom, north, south, east, west

    # 범위 체크
    temp_x = x
    temp_y = y-1
    if check(temp_x, temp_y):

        # 1. 주사위 변형(서쪽)
        temp_bottom = bottom
        bottom = west
        west = top
        top = east
        east = temp_bottom

        # 2. 주사위 변형 값으로 그래프 변형
        if (graph[temp_x][temp_y] == 0):
            graph[temp_x][temp_y] = bottom
        else:
            bottom = graph[temp_x][temp_y]
            graph[temp_x][temp_y] = 0

        return temp_x, temp_y
    else:
        return x, y

def north_move(x,y):
    global top, bottom, north, south, east, west

    # 범위 체크
    temp_x = x-1
    temp_y = y
    if check(temp_x, temp_y):

        # 1. 주사위 변형(북쪽)
        temp_bottom = bottom
        bottom = north
        north = top
        top = south
        south = temp_bottom

        # 2. 주사위 변형 값으로 그래프 변형
        if (graph[temp_x][temp_y] == 0):
            graph[temp_x][temp_y] = bottom
        else:
            bottom = graph[temp_x][temp_y]
            graph[temp_x][temp_y] = 0

        return temp_x, temp_y
    else:
        return x, y

def south_move(x,y):
    global top, bottom, north, south, east, west

    # 범위 체크
    temp_x = x+1
    temp_y = y
    if check(temp_x, temp_y):

        # 1. 주사위 변형(남쪽)
        temp_bottom = bottom
        bottom = south
        south = top
        top = north
        north = temp_bottom

        # 2. 주사위 변형 값으로 그래프 변형
        if (graph[temp_x][temp_y] == 0):
            graph[temp_x][temp_y] = bottom
        else:
            bottom = graph[temp_x][temp_y]
            graph[temp_x][temp_y] = 0

        return temp_x, temp_y
    else:
        return x, y

def move(number,x,y):
    # 동쪽
    if number == 1:
        return east_move(x,y)
    
    # 서쪽
    elif number == 2:
        return west_move(x,y)
    
    # 북쪽
    elif number == 3:
        return north_move(x,y)
    
    # 남쪽
    elif number == 4:
        return south_move(x,y)
    
# 입력
n,m,x,y,k = map(int,input().split())
graph = [-1 for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int,input().split()))

info_list = list(map(int,input().split()))

# 계산1: 주사위 정보
top = 0
bottom = 0
north = 0
south = 0
west = 0
east = 0

# 계산2: 명령
cur_x = x
cur_y = y
for info in info_list:

    next_x, next_y = move(info, cur_x, cur_y)
    if (next_x == cur_x and next_y == cur_y):
        pass
    else:
        print(top)

    cur_x = next_x
    cur_y = next_y