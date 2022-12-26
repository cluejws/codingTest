def union(x,y):
    root_x = find(x)
    root_y = find(y)
    
    if root_x != root_y:
        parent[root_y] = root_x
        
def find(x):
    
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return parent[x]

def print_group(x,y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        print("YES")
    else:
        print("NO")
    
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    if a == 0:
        union(b,c)
    elif a == 1:
        print_group(b,c)