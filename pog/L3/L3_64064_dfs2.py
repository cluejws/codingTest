def check(bid, uid):
    
    # 1.
    if len(bid) != len(uid):
        return False
    
    # 2.
    n = len(bid)
    for i in range(n):
        if bid[i] != uid[i] and bid[i] != '*':
            return False
        
    return True
        
def solution(user_id, banned_id):
    
    # 계산1: banned_id 딕셔너리 생성
    dict_b = {}
    for bid in banned_id:
        
        # 1.
        if bid in dict_b:
            continue
        
        # 2.
        for uid in user_id:
            if check(bid, uid):
                if bid in dict_b:
                    dict_b[bid].append(uid)
                else:
                    dict_b[bid] = [uid]

    # 계산2: 조합
    def dfs(start):
        if len(arr) == n:
            
            # -> 정렬을 통해 중복 제거
            # -> 집합을 통해 중복 제거
            if set(arr) not in list_arr:
                list_arr.append(set(arr))
            return

        for i in range(start, n):
            uid_list = dict_b[banned_id[i]]
            for uid in uid_list:
                if uid not in arr:
                    arr.append(uid)
                    dfs(i+1)
                    arr.pop()
        
    n = len(banned_id)
    arr = []
    list_arr = []
    dfs(0)
  
    return len(list_arr)