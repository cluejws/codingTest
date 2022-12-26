import copy

# 회전 경우마다 전체 톱니바퀴 변화
def all_move(point, dir):
    temp = copy.deepcopy(graph)
    
    temp0_right = temp[0][2]

    temp1_left = temp[1][6]
    temp1_right = temp[1][2]
    
    temp2_left = temp[2][6]
    temp2_right = temp[2][2]
    
    temp3_left = temp[3][6]

    if point == 0:
        
        # point 오른쪽
        if temp0_right == temp1_left:
            if dir == 1:
                clock_move(graph[0])
            else:
                reverse_move(graph[0])
        else:
            if dir == 1:
                clock_move(graph[0])
                reverse_move(graph[1]) 
                if temp1_right == temp2_left:
                    pass 
                else:
                    clock_move(graph[2])
                    if temp2_right == temp3_left:
                        pass 
                    else:
                        reverse_move(graph[3])
            else:
                reverse_move(graph[0])
                clock_move(graph[1])
                if temp1_right == temp2_left:
                    pass 
                else:
                    reverse_move(graph[2])
                    if temp2_right == temp3_left:
                        pass
                    else:
                        clock_move(graph[3])
    elif point == 1:
        
        # point 왼쪽
        if temp1_left == temp0_right:
            if dir == 1:
                clock_move(graph[1])
            else:
                reverse_move(graph[1])
        else:
            if dir == 1:
                clock_move(graph[1])
                reverse_move(graph[0])
            else:
                reverse_move(graph[1])
                clock_move(graph[0])
        
        # point 오른쪽        
        if temp1_right == temp2_left:
            pass
        else:
            if dir == 1:
                reverse_move(graph[2])
                if temp2_right == temp3_left:
                    pass
                else:
                    clock_move(graph[3])
            else:
                clock_move(graph[2])
                if temp2_right == temp3_left:
                    pass
                else:
                    reverse_move(graph[3])
                
    elif point == 2:
        
        # point 왼쪽
        if temp2_left == temp1_right:
            if dir == 1:
                clock_move(graph[2])
            else:
                reverse_move(graph[2])
        else:
            if dir == 1:
                clock_move(graph[2])
                reverse_move(graph[1])
                if temp1_left == temp0_right:
                    pass
                else:
                    clock_move(graph[0])
            else:
                reverse_move(graph[2])
                clock_move(graph[1])
                if temp1_left == temp0_right:
                    pass
                else:
                    reverse_move(graph[0])
        
        # point 오른쪽        
        if temp2_right == temp3_left:
            pass
        else:
            if dir == 1:
                reverse_move(graph[3])
            else:
                clock_move(graph[3])
    else:
        
        # point 왼쪽
        if temp3_left == temp2_right:
            if dir == 1:
                clock_move(graph[3])
            else:
                reverse_move(graph[3])
        else:
            if dir == 1:
                clock_move(graph[3])
                reverse_move(graph[2])
                if temp2_left == temp1_right:
                    pass
                else:
                    clock_move(graph[1])
                    if temp1_left == temp0_right:
                        pass
                    else:
                        reverse_move(graph[0])
            else:
                reverse_move(graph[3])
                clock_move(graph[2])
                if temp2_left == temp1_right:
                    pass
                else:
                    reverse_move(graph[1])
                    if temp1_left == temp0_right:
                        pass
                    else:
                        clock_move(graph[0])
        
# 해당 톱니바퀴 -> 시계방향으로 회전
def clock_move(arr):
    temp_arr = copy.deepcopy(arr)
    
    temp_end = temp_arr[-1]
    for i in range(len(arr)-1):
        arr[i+1] = temp_arr[i]
    arr[0] = temp_end

# 해당 톱니바퀴 -> 반시계방향으로 회전
def reverse_move(arr):
    temp_arr = copy.deepcopy(arr)
    
    temp_start = temp_arr[0]
    for i in range(len(arr)-2, -1, -1):
        arr[i] = temp_arr[i+1]
    arr[-1] = temp_start

# 입력
# S극:1 N극:0
graph = [list(map(int,input())) for _ in range(4)]

# dir(1)=시계 dir(-1)=반시계
k = int(input())
for _ in range(k):
    n, dir = map(int,input().split())
    all_move(n-1, dir)

# 점수계산
res = 0
if graph[0][0] == 1:
    res += 1
if graph[1][0] == 1:
    res += 2
if graph[2][0] == 1:
    res += 4
if graph[3][0] == 1:
    res += 8
print(res)
