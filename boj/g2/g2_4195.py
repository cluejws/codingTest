def union(a,b):
    root_a = find(a)
    root_b = find(b)
    
    if root_a != root_b:
        parent[root_b] = root_a
        network[root_a] += network[root_b]
        network[root_b] = network[root_a]
    
    return network[root_a]
                
def find(x):
    
    if x == parent[x]:
        return x

    else:
        y = find(parent[x])
        parent[x] = y
        return y

t = int(input())
for _ in range(t):
    
    # 초기 조건
    f = int(input()) 
    parent = {}
    network = {}
    
    # 입력 모든 관계
    for _ in range(f):
        
        a,b = input().split()
        if a not in parent:
            parent[a] = a
            network[a] = 1
        if b not in parent:
            parent[b] = b
            network[b] = 1
            
        print(union(a,b))
        