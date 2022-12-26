def DFS(graph, x, y , visited):
      
  visited[x][y] = 1
  
  # 단지내 집 수 세기
  if graph[x][y] == 1:
    global apt_count
    apt_count += 1
  
  # 상하좌우로 DFS진행
  for t in range(4):
    temp_x = x + dx[t]
    temp_y = y + dy[t]
  
    if check(temp_x,temp_y) and visited[temp_x][temp_y] == 0 and graph[temp_x][temp_y] == 1:
      DFS(graph, temp_x, temp_y, visited)

def check(i,j):
  global n
  if 0<=i<=n-1 and 0<=j<=n-1:
    return True
  else:
    return False

# 입력
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
  t = input().split()
  graph.append(list(map(int,list(t[0]))))

visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]


# 계산
apt_count = 0
apt_list = []
for i in range(len(graph)):
  for j in range(len(graph[0])):
    if visited[i][j] == 0 and graph[i][j] == 1:
      DFS(graph, i, j ,visited)
      apt_list.append(apt_count)
      apt_count = 0

# 출력
print(len(apt_list))
apt_list.sort()
for apt in apt_list:
  print(apt)

