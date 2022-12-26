def setParent(a):
    for i in graph[a]:
        if parent[i] == -1 and i != -1:
            parent[i] = a
            setParent(i)

# 입력
import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 계산
# 계산1: dfs(1)로 초기화
setParent(1)

# 계산2: dfs()로 부모 얻기
for i in range(2,n+1):
    print(parent[i])


