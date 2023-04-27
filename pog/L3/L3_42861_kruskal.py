min_res = 0

def solution(n, costs):
    
    # union
    def union(a,b):
    
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a
            return True

        return False
    
    # find
    def find(x):
    
        if x == parent[x]:
            return x
    
        p = find(parent[x])
        parent[x] = p
        return parent[x]
    
    # 계산1: 최소 얻기 위해 cost정렬
    costs.sort(key=lambda x: (x[2]))
    
    # 계산2: kruskal
    global min_res
    parent = [i for i in range(n)]
    
    for a,b,cost in costs:
        if union(a,b):
            min_res += cost
        
    return min_res