def getResult(orders, c):
    
    # 백트래킹
    def backTracking(order, cnt, start):
        if cnt == c:
            combi = ''.join(arr)
            if combi in dict_res:
                dict_res[combi] += 1
            else:
                dict_res[combi] = 1
            return
        
        for i in range(start, len(order)):
            arr.append(order[i])
            backTracking(order, cnt + 1, i + 1)
            arr.pop()    
    
    # 계산1: 백트래킹
    dict_res = {}
    for order in orders:
        arr = []
        backTracking(order, 0, 0)
    
    # 계산2: 딕셔너리 정렬
    sortedItems = sorted(dict_res.items(), key = lambda x: x[1], reverse=True)

    # 계산3: 최대값 가지는 요소 return
    if len(sortedItems) > 0:
        
        maxItems = []
        for i in range(len(sortedItems)):
            if sortedItems[0][1] > 1 and sortedItems[i][1] == sortedItems[0][1]:
                maxItems.append(sortedItems[i][0])
        return maxItems
    else:
        return []

def solution(orders, course):
    
    # 계산0: orders 사전 순 정렬
    sortedOrders = []
    for order in orders:
        sortedOrders.append(sorted(order))
    
    # 계산1: 반영
    answer = []
    for c in course:
        # 1. 최대값 가지는 요소
        res = getResult(sortedOrders, c)
        
        # 2. 결과 반영
        for r in res:
            answer.append(r)
    
    # 계산2: 정렬
    answer.sort()
    
    return answer