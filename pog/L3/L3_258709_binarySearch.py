def makeCombination(n, k):
    def dfs(cnt, idx):
        if cnt == k:
            result.append(set(temp))
            return
        
        for i in range(idx, n):
            temp.append(i)
            dfs(cnt + 1, i + 1)
            temp.pop()
            
    result = []
    temp = []
    dfs(0, 0)
    
    return result

def getResult(dice, set_combi):
    def dfs(cnt):
        if cnt == k:
            # 1. 주사위 조합 경우, 합 조합
            sum_res = 0
            for i in range(k):
                sum_res += (dice[combi[i]][temp[i]])
            
            # 2.
            if sum_res not in result:
                result[sum_res] = 1
            else:
                result[sum_res] += 1
            return
            
        for i in range(6):
            temp.append(i)
            dfs(cnt + 1)
            temp.pop()
    
    # 1.
    combi = list(set_combi)
    k = len(combi)
    
    # 2.
    result = {}
    temp = []
    dfs(0)
    
    return result

def getWinCount(a_dict, b_dict):
    # 계산1: 정렬
    a_items = list(a_dict.items())
    a_items.sort()
    b_items = list(b_dict.items())
    b_items.sort()

    # 계산2: a 순회(이진탐색)
    win_cnt = 0
    for a_value, a_cnt in a_items:
        
        # 2-1: 이진탐색(해당 숫자 미만인 가장 큰 숫자)
        n = len(b_items)
        
        max_idx = -1
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            b_value, b_cnt = b_items[mid]
            if b_value < a_value:
                max_idx = max(max_idx, mid)
                left = mid + 1
            else:
                right = mid - 1
        
        # 2-2: 이진탐색 반영
        b_value, b_cnt = b_items[0]
        if a_value < b_value:
            win_cnt += (0 * b_cnt)
        else:
            for idx in range(max_idx+1):
                b_value, b_cnt = b_items[idx]
                win_cnt += (a_cnt * b_cnt) 
    
    return win_cnt

def solution(dice):
    # 계산1: 주사위 조합
    n = len(dice)
    combis = makeCombination(n, n//2)  
    
    # 계산2
    max_cnt = 0
    max_res = []
    for a_combi in combis:
        # 2-1: b 주사위 조합
        b_combi = set(range(n)) - a_combi
        
        # 2-2: a 주사위 조합 경우, 결과
        # 2-2: b 주사위 조합 경우, 결과
        a_dict = getResult(dice, a_combi)
        b_dict = getResult(dice, b_combi)
        
        # 2-3: 최대 승리 반영
        win_cnt = getWinCount(a_dict, b_dict)
        if max_cnt < win_cnt:
            max_cnt = win_cnt
            max_res = list(map(lambda x: x+1, list(a_combi)))

    return max_res