def DFS(graph, x, visited, group):
  visited[x] = group
  for i in range(len(graph[x])):
    y = graph[x][i]

    # 기저조건: 같은 그룹이면 빠져나오고/ 나머지 재귀는 진행
    if visited[y] != 0 and visited[y] == group:
        global flag
        flag = False
        return

    # 재귀: 반대 그룹으로 넣기위해 div_group생성
    if group == 1: div_group = -1
    elif group == -1: div_group = 1

    if visited[y] == 0:
        DFS(graph, y, visited, div_group)


# 입력
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  
    v, e = map(int,input().split())

    graph = [[] for _ in range(v)]
    visited = [0 for _ in range(v)]
    
    for _ in range(e):
        i,k = map(int,input().split())
        graph[i-1].append(k-1)
        graph[k-1].append(i-1)
    
    # 계산
    flag = True
    for m in range(0, v):
        if visited[m] == 0:
            DFS(graph,m,visited,1)
            if not flag:
                break
    
    if flag == True:
      print("YES")
    else:
      print("NO")