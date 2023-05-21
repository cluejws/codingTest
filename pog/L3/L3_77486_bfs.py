from collections import deque

def solution(enroll, referral, seller, amount):
    
    # 계산1: 딕셔너리 생성 -> 이름, index
    dict_e = {}    
    n = len(enroll)
    for i in range(n):
        dict_e[enroll[i]] = i+1

    # 계산2: 그래프 생성
    graph = [[] for _ in range(n+1)]
    for i in range(n):
        if referral[i] == '-':
            continue
            
        graph[dict_e[enroll[i]]].append(dict_e[referral[i]])

    # 계산3: bfs
    def bfs(i):
        
        queue = deque()
        queue.append((dict_e[seller[i]], int(amount[i] * 100 * 0.1)))
        result[dict_e[seller[i]]] += (amount[i] * 100 - int(amount[i] * 100 * 0.1))
        
        while len(queue) > 0:
            x, price = queue.popleft()
            for y in graph[x]:
                
                # 1. 10% 금액이 1원 미만 경우 분배X
                if price < 10:
                    result[y] += round(price)
                    break
                
                # 2.
                queue.append((y, int(price * 0.1)))
                result[y] += (price - int(price * 0.1))

    # seller 순회하면서 bfs
    result = [0 for _ in range(n+1)]
    m = len(seller)
    for i in range(m):
        bfs(i)

    return result[1:]