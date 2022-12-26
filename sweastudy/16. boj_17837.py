def check(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else: return False

# 입력(graph: 흰=0 빨=1 파=2) 
n,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[[] for _ in range(n)] for _ in range(n)]

# 입력(piece_arr -> 위치, 방향)
# 입력(visited   -> 말 번호)
piece_arr = []
for idx in range(k):
    i,j,dir = map(int,input().split())
    piece_arr.append([i-1,j-1, dir-1])
    visited[i-1][j-1].append(idx)

# 방향 전환
dx = [0,0,-1,1]
dy = [1,-1,0,0]
    
def reverse_dir(dir):
    
    if dir == 0:
        return 1
    elif dir == 1:
        return 0
    elif dir == 2:
        return 3
    elif dir == 3:
        return 2
    
# 1개의 말 움직임
# return True면 정상적으로 움직임
# return False면 이제 끝
def piece_move(piece_number):
    
    cur_x,cur_y,cur_dir = piece_arr[piece_number]
    
    next_x = cur_x + dx[cur_dir]
    next_y = cur_y + dy[cur_dir]
        
    if not check(next_x, next_y) or graph[next_x][next_y] == 2: # 벽 or 파랑
        
        # 계산0: 방향 전환 후 next_x, next_y 초기화
        cur_dir = reverse_dir(cur_dir)
        piece_arr[piece_number][2] = cur_dir
          
        next_x = cur_x + dx[cur_dir]
        next_y = cur_y + dy[cur_dir]
        
        
        # 기저조건: 방향 전환을 했는데도 벽 or 파랑
        # 다른 말 신경 쓸 필요 X      
        if not check(next_x,next_y) or graph[next_x][next_y] == 2:
            return True
        
    if graph[next_x][next_y] == 0:
    
        # 계산1: 이전위치 갱신 & 위에쌓인 말 얻기
        temp_arr = [] 
        for i, piece_idx in enumerate(visited[cur_x][cur_y]):
            if piece_idx == piece_number:
                temp_arr.extend(visited[cur_x][cur_y][i:])
                visited[cur_x][cur_y] = visited[cur_x][cur_y][:i]
                break
        
        # 계산2: 위에 쌓인 말을 통해 이후위치 갱신 
        for piece_idx in temp_arr:
            piece_arr[piece_idx][0] = next_x
            piece_arr[piece_idx][1] = next_y
            visited[next_x][next_y].append(piece_idx)
        
        # 계산3: 이후위치 갱신 후 멈춤판단                    
        if len(visited[next_x][next_y]) >= 4:
            return False
        
    elif graph[next_x][next_y] == 1:
        
        # 계산1: 이전위치 갱신 & 위에쌓인 말 얻기
        temp_arr = [] #(위에쌓인 말)
        for i, piece_idx in enumerate(visited[cur_x][cur_y]):
            if piece_idx == piece_number:
                temp_arr.extend(visited[cur_x][cur_y][i:])
                visited[cur_x][cur_y] = visited[cur_x][cur_y][:i]
                break
        
        # 빨강이라 reverse
        temp_arr.reverse()    
        
        # 계산2: 위에 쌓인 말을 통해 이후위치 갱신 
        for piece_idx in temp_arr:
            piece_arr[piece_idx][0] = next_x
            piece_arr[piece_idx][1] = next_y
            visited[next_x][next_y].append(piece_idx)
        
        # 계산3: 이후위치 갱신 후 멈춤판단                    
        if len(visited[next_x][next_y]) >= 4:
            return False
    return True
    
# 계산
count = 0
while True:
    
    if count > 1000:
        print(-1)
        quit()
    
    
    is_break = False
    # 모든 말 순회    
    for piece_number in range(k):
        
        if piece_move(piece_number) == False:
            is_break = True
            break
    
    count += 1
    if is_break == True:
        print(count)
        quit()
