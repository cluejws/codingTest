def check(x, y, x1, y1, x2, y2):
    if (x1-1<=x<=x2-1) and (y1-1<=y<=y2-1):
        return True
    
    return False

def getGraph(n, m):

    graph = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(m):
            cnt += 1
            graph[x][y] = cnt
    
    return graph

def setGraph(query, graph, n, m):
    
    # 1. 환경 구축
    x1, y1, x2, y2 = query    
    returnGraph = [item[:] for item in graph]
    visited = [[False for _ in range(m)] for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    # 2. 회전 초기화(시작x,y / 이전값 / 방향)
    x, y = x1-1, y1-1
    value = graph[x][y]
    dir_num = 0
    
    # 3. 회전 + 최소값
    min_value = value
    for _ in range((x2-x1+1) * (y2-y1+1)):
        
        # 1. 방향 설정
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        if not check(nx,ny,x1,y1,x2,y2):
            dir_num = (dir_num + 1) % 4
        
        # 2. 방문 판단
        if visited[x+dx[dir_num]][y+dy[dir_num]] == True:
            break
        
        # 3. 방향 설정 후 위치 설정
        # 회전(이전값 반영 / 이전값 초기화 / 방문 처리)
        # 최소값
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        
        returnGraph[x][y] = value
        value = graph[x][y]
        visited[x][y] = True
        
        min_value = min(min_value, value)
    

    return returnGraph, min_value
    
def solution(rows, columns, queries):
    
    # 계산1: 기본 그래프 생성
    graph = getGraph(rows, columns)

    # 계산2: 
    # query 마다 회전 반영
    # query 마다 최소값 얻기
    res = []
    for query in queries:
        graph, min_res = setGraph(query, graph, rows, columns)
        res.append(min_res)
    
    return res