def dfs(cnt, next):
    
    # 기저조건1: 약품넣는게 이미 많으면 안됨
    global res, w
    if cnt >= res:
        return 
    
    # 기저조건2: 검사 만족했는지? 후 할당
    if check():
        if res > cnt :
            res = cnt
        return
       
    # 완전탐색
    for i in range(next, d):
        for dg in range(2):
            
            graph[i] = [dg for _ in range(w)]
            
            dfs(cnt+1, i+1)
            
            graph[i] = original_graph[i] 


def check():
    for y in range(w):
        
        cnt = 1
        for x in range(d-1):
            if graph[x][y] == graph[x+1][y]:
                cnt += 1
            else:
                cnt = 1
            
            if cnt >= k:
                break
            
        if cnt < k:
            return False
        
    return True
    
# 입력
import sys,math
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    d,w,k = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(d)]
    original_graph = list(graph)

    print(graph, original_graph)
    # 계산
    res = math.inf
    
    if check():
        res = 0
    else:
        dfs(0,0)
    
    # 출력
    print(f"#{tc+1} {res}")
    
