def check(x,y):
    if 0<=x<h+1 and 0<=y<(2*n)-1:
        return True
    else:
        return False

def is_same():
    for j in range(0, (2*n)-1, 2):
        x,y = 0,j
    
        while True:

            if x == h:
                break
            
            if check(x,y-1) and graph[x][y-1] == 1:
                while True:
                    if check(x,y-1) and graph[x][y-1] == 1:
                        y -= 1
                    else:
                        x += 1
                        break
            elif check(x,y+1) and graph[x][y+1] == 1:
                while True:
                    if check(x,y+1) and graph[x][y+1] == 1:
                        y += 1
                    else:
                        x += 1
                        break
            else:
                x += 1 
     
        if y != j: return False
    return True
               
def getResult(depth, index):
        
    # 기저조건1: 사다리추가하는게 이미 많으면 안됨
    global res
    if depth >= res: 
        return 
    
    
    # 기저조건2: 사다리조건 만족했는지? 후 할당
    if is_same():
        res = depth  
        return
    
    # 완전탐색
    for i in range(index, len(plus)): 
        x, y = plus[i]
        
        graph[x][y] = 1
        getResult(depth+1, i+1)
        graph[x][y] = 0
         
            
import sys
input = sys.stdin.readline

# 입력
# n:세로틀 m:놓는 가로선 수 h:가로틀
# graph: 세로틀:h+1 가로틀:2*n-1

n,m,h = map(int,input().split())
graph = [[0 for _ in range(2*n-1)] for _ in range(h+1)]
for i in range(h+1):
    for j in range(0,2*n-1,2):
        graph[i][j] = 1

for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1][2*b-1] = 1


# 사다리 후보군 넣기
plus = []
for i in range(h):
    for j in range(1,2*n-1,2):
        if graph[i][j] == 0:
            plus.append([i,j])    

# 계산
res = 4
getResult(0,0) # depth=0(아무것도 안넣고), idx(처음후보군부터)

# 출력
if res < 4:
    print(res)
else:
    print(-1)