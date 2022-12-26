def check(x,y):
    if 0<=x<100 and 0<=y<100:
        return True
    else: return False

import sys
input = sys.stdin.readline

for _ in range(10):
    t = int(input())
    graph = [list(map(int,input().split())) for _ in range(100)]
    
    # end: x, y 찾기
    x,y = -1,-1
    for j in range(100): 
        if graph[99][j] == 2:
            x,y = 98, j
            break
    
    # 올라가기
    while True:
        
        if x == 0:
            print(f"#{t} {y}")
            break
        
        # 왼쪽이동, 오른쪽이동, 위로이동
        
        if check(x,y-1) and graph[x][y-1] == 1:
            
            while True: # 0을 만날 때 까지 계속 이동
                
                if check(x,y-1) and graph[x][y-1] == 1: 
                    y -= 1
                else:
                    x -= 1
                    break  
        elif check(x,y+1) and graph[x][y+1] == 1:
            
            while True: # 0을 만날 때 까지 계속 이동
                if check(x,y+1) and graph[x][y+1] == 1: 
                    y += 1
                else:
                    x -= 1
                    break
        else:
            x -= 1
               

        
            

                
        

                
     
    
            
    
        