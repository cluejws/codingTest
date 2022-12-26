def dfs(cnt, move): # cnt: 해당시점의 최대값 move: 이동시킨횟수
    
    # 기저조건1: 최대5번 이동가능 후 할당
    if move > 5:
        return

    global graph, res    
    if cnt > res:
        res = cnt
    
    for i in range(4):

        # 그래프 변형O
        temp_graph = copy.deepcopy(graph)
        getMove(i)
        
        # 최대값구해서 -> dfs
        value = max(map(max,graph))
        dfs(value, move+1)
        
        # 그래프 이전 값으로 돌아가야됨 
        graph = copy.deepcopy(temp_graph)

# 그래프 변형 
def getMove(k):
    
    # (1) 그래프 변형
    if k == 0:   # 아래로
        
        for j in range(n): # 모든 열
        
            end = n-1
            for i in range(n-2, -1, -1):
                
                if graph[i][j] != 0:
                    
                    temp = graph[i][j]
                    
                    graph[i][j] = 0

                    if graph[end][j] == 0:          # 다음것이 0일때(end가 0일때 / end와 swap)
                        graph[end][j] = temp
                    
                    elif graph[end][j] == temp:     # 다음것이 같을때(end와 같을때 / end에 multi)
                        graph[end][j] = temp * 2
                        end -= 1
                    else:                           # 다음것이 다를때(end와 다를때 / end-1에 할당)
                        end -= 1
                        graph[end][j] = temp 
        
                
    elif k == 1:  # 위로
        
        for j in range(n): # 모든 열
        
            end = 0
            for i in range(1,n):
                
                if graph[i][j] != 0:
                    
                    temp = graph[i][j]
                    
                    graph[i][j] = 0
                    
                    if graph[end][j] == 0:          # 다음것이 0일때(end가 0일때 / end와 swap)
                        graph[end][j] = temp
                    
                    elif graph[end][j] == temp:     # 다음것이 같을때(end와 같을때 / end에 multi)
                        graph[end][j] = temp * 2
                        end += 1
                    else:                           # 다음것이 다를때(end와 다를때 / end-1에 할당)
                        end += 1
                        graph[end][j] = temp 
        
    elif k == 2: # 오른쪽으로
        
        for i in range(n): # 모든 행
        
            end = n-1
            for j in range(n-2, -1, -1):
                
                if graph[i][j] != 0:
                    
                    temp = graph[i][j]
                    
                    graph[i][j] = 0
                    
                    if graph[i][end] == 0:         # 다음것이 0일때(end가 0일때 / end와 swap)
                        graph[i][end] = temp
                    
                    elif graph[i][end] == temp:    # 다음것이 같을때(end와 같을때 / end에 multi)
                        graph[i][end] = temp * 2
                        end -= 1
                    else:                          # 다음것이 다를때(end와 다를때 / end-1에 할당)
                        end -= 1
                        graph[i][end] = temp 
        
    else:        # 왼쪽으로
        
        for i in range(n): # 모든 행
            
            end = 0
            for j in range(1,n):

                if graph[i][j] != 0:

                    temp = graph[i][j]

                    graph[i][j] = 0

                    if graph[i][end] == 0:         # 다음것이 0일때(end가 0일때 / end와 swap)
                        graph[i][end] = temp

                    elif graph[i][end] == temp:    # 다음것이 같을때(end와 같을때 / end에 multi)
                        graph[i][end] = temp * 2
                        end += 1
                    else:                          # 다음것이 다를때(end와 다를때 / end-1에 할당)
                        end += 1
                        graph[i][end] = temp 
    

# 입력
import sys, copy
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split()))for _ in range(n)]

# 아래로:0 위로:1 오른쪽:2 왼쪽3
#print(getMove(2))
#print(getMove(0))
#print(getMove(0))
#print(getMove(1))
#print(getMove(2))
#print(getResult())

# 계산
res = 0
dfs(0,0) # cnt, move

# 출력
print(res)