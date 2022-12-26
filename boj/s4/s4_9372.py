def union(a,b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a
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
        
def kruskal():
    
    global res
    for edge in edgelist:
        if union(edge[0],edge[1]):
            res += 1

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    n,m = map(int,input().split())
    
    parent = [i for i in range(n+1)]
    edgelist = []
    
    for _ in range(m):
        a,b = map(int,input().split())
        edgelist.append((a,b))
    
    res = 0
    kruskal()
    print(res)
