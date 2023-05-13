def solution(n, computers):
    
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        
        if root_a != root_b:
            network[root_b] = root_a
        
    def find(x):
        if x == network[x]:
            return x
        
        y = find(network[x])
        network[x] = y
        return network[x]
    
    # 계산1: 네트워크 얻기 -> unionFind
    network = [i for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):                
            if computers[i][j] == 1:
                union(i, j)

    # 계산2: 네트워크 세기 -> 네트워크 집합화
    set_network = set()
    for i in range(n):
        root_i = find(i)
        set_network.add(root_i)

    # 출력
    return len(set_network)