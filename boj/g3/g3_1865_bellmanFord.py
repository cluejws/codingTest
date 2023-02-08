def bellmanFord(start):
    
    # 계산1: 시작노드 초기화X
    # (랜덤으로 벨만포드 시작점 설정)
    # (INF 사용하지 않고 임의의 최대수로 설정)
    dist = [200000000 for _ in range(n+1)]
    
    # 계산2: 변형 벨만포드
    for i in range(n):
        for j in range(len(edges)):
            
            cur_index = edges[j][0]
            next_index = edges[j][1]
            cost = edges[j][2]
            
            # 이미 처음부터 모든 정점을 방문한 걸로 착각
            # 음수 사이클이 어디에 있든 항상 도달이 가능
            if dist[next_index] > dist[cur_index] + cost:
                dist[next_index] = dist[cur_index] + cost
                
                # 음수 순환 존재 시 stop
                if i == n-1:
                    return False

    return True


import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    
    # 입력
    n, m, w = map(int,input().split())
    edges = []
    
    for _ in range(m):
        s,e,t = map(int,input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
    
    for _ in range(w):
        s,e,t = map(int,input().split())
        edges.append((s,e,-t))
        
    
    # 계산: 벨만포드(랜덤 시작점: 음수 순환 포함 판단)
    res = bellmanFord(1)
    
    # 출력:
    if res == False:
        print('YES')
    else:
        print('NO')