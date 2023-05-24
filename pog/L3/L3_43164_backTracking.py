def solution(tickets):
    
    # dfs
    def dfs(x):
        if len(path) == n+1:
            res_path.append(path[:])
            return
        
        for i in range(n):
            start, end = tickets[i]
            if start == x and visited[i] == False:            
                visited[i] = True
                path.append(end)
                dfs(end)
                path.pop()
                visited[i] = False
    
    # 계산1: dfs(경로 백트래킹 -> 경로 경우의 수)
    n = len(tickets)
    visited = [False for _ in range(n)]
    res_path = []
    path = ['ICN']
    
    dfs('ICN')
    
    # 계산2: (배열->문자열) 오름차순 정렬
    res_path.sort(key = lambda path: (''.join(path)))
    return res_path[0]
    