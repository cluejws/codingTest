def kruskal():
  
  for i in range(m):
    if union(edgelist[i][0], edgelist[i][1]):
      global cost
      cost += edgelist[i][2]
    else:
      continue
  
def union(a,b):
  
  root_a = find(a)
  root_b = find(b)
  
  if root_a != root_b:
    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    elif rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a
        rank[root_a] += 1
    return True
  else:
    return False
    
def find(x):
  
  if x == parent[x]:
    return x
    
  else:
    y = find(parent[x])
    parent[x] = y
    return parent[x]

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]
edgelist = []

for _ in range(m):
  a,b,c = map(int,input().split())
  edgelist.append((a,b,c))
edgelist.sort(key=lambda x: x[2])

cost = 0
kruskal()
print(cost)
