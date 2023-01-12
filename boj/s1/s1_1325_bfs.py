def getCount(node):
    
    visited = [False for _ in range(n+1)]
    
    # 계산1: bfs
    queue = deque()
    queue.append(node)
    
    visited[node] = True
    
    while len(queue) != 0:
        cur_node = queue.popleft()
        
        for i in range(len(graph[cur_node])):
            next_node = graph[cur_node][i]
            if visited[next_node] == False:
                queue.append(next_node)
                visited[next_node] = True
                
    # 계산2: 연결 노드 수 얻기
    cnt = 0
    for visit in visited:
        if visit == True:
            cnt += 1
    
    return cnt
    
# 입력
from collections import deque

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

# 계산: 노드 마다 bfs 돌려서 / 연결 노드 수 얻기 
index_arr = []
max_cnt = 0
for i in range(1, n+1):
    
    # 계산1: bfs 후 연결 노드수 얻기
    cnt = getCount(i)

    # 계산2: 최대 연결 노드수를 가지는 index 얻기
    if cnt > max_cnt:
        max_cnt = cnt
        
        index_arr = []
        index_arr.append(i)

    elif cnt == max_cnt:
        index_arr.append(i)

# 출력 
print(' '.join(list(map(str, index_arr))))