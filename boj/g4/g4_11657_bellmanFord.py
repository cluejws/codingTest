def bellmanFord(start):
    
    # 계산1: 시작노드 초기화
    dist[start] = 0
    
    # 계산2: 벨만포드
    for i in range(n):
        for j in range(m):
            
            cur_index = edges[j][0]
            next_index = edges[j][1]
            cost = edges[j][2]
            
            if dist[cur_index] != math.inf and dist[next_index] > dist[cur_index] + cost:
                dist[next_index] = dist[cur_index] + cost
                
                # 음수 순환 존재 시 stop
                if i == n-1:
                    return False

    return True
            
# 입력
import sys, math
input = sys.stdin.readline

n, m = map(int,input().split())
edges = []
dist = [math.inf for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))
    
# 계산: 벨만포드(1번정점)
res_1 = bellmanFord(1)

# 출력
if res_1:
    for i in range(2, n+1):
        if dist[i] == math.inf:
            print(-1)
        else:
            print(dist[i])
else:
    print(-1)