def rotate(point_x,point_y, x,y): 
    # 일반적인 x,y축 -> 시계방향90 = -90
    # 현재 x,y축     -> 시계방향90 = 90
    c = 0
    s = 1
    res_x = c*(x-point_x)-s*(y-point_y) + point_x
    res_y = s*(x-point_x)+c*(y-point_y) + point_y

    graph[res_x][res_y] = 1
    return (res_x,res_y)            

# 입력
n = int(input())
graph = [[-1 for _ in range(101)] for _ in range(101)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

# 입력받으면서 계산
for _ in range(n):
    
    path = []
    
    # 계산1 : 입력 및 시작, 끝점 할당
    x,y,d,g = map(int,input().split())
    end_x = x + dx[d]
    end_y = y + dy[d]
    
    path.append((x,y))
    path.append((end_x,end_y))
    graph[x][y] = 1
    graph[end_x][end_y] = 1
    
    
    # 계산2 : 세대만큼 시계방향으로 90도 회전반복
    for _ in range(g):
        
        rotate_path = []
        point_x, point_y = path[-1]

        for idx in range(len(path)-2, -1, -1):
            path_x, path_y = path[idx]
            rotate_path.append(rotate(point_x,point_y, path_x,path_y))

        path.extend(rotate_path)

# 계산
cnt = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
            cnt += 1

# 출력
print(cnt)     