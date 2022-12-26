import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,group):
    visited[x] = group
    for i in range(len(graph[x])):
        y = graph[x][i]
        if visited[y] == -1:
            dfs(y, group)

# 입력
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 계산: cnt로 group판별, 0노드 제외
cnt = 0
for k in range(1,n+1):
    if visited[k] == -1:
        dfs(k,cnt)
        cnt += 1
        
# 출력
print(cnt)