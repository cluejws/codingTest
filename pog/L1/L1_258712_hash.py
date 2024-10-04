def makeCombination(arr):
    def dfs(cnt, idx):
        if cnt == 2:
            result.append(set(temp))
            return
        
        for i in range(idx, n):
            temp.append(arr[i])
            dfs(cnt + 1, i + 1)
            temp.pop()
    
    # 1. 
    n = len(arr)
    
    result = []
    temp = []
    dfs(0, 0)
    
    return result

def solution(friends, gifts):
    # 계산1: 선물 기록 순회로, 선물 기록/선물 지수
    dict_gift = {}
    dict_friend_point = {}
    for gift in gifts:
        a, b = gift.split()
        
        # 1-1: 선물 기록
        if (a,b) not in dict_gift:
            dict_gift[(a,b)] = 1
        else:
            dict_gift[(a,b)] += 1
        
        # 1-2: 선물 지수
        if a not in dict_friend_point:
            dict_friend_point[a] = 1
        else:
            dict_friend_point[a] += 1
        
        if b not in dict_friend_point:
            dict_friend_point[b] = -1
        else:
            dict_friend_point[b] -= 1

    # 계산2: 결과 수
    dict_cnt = {}
    for friend in friends:
        dict_cnt[friend] = 0
    
    # 계산3: 사람 조합
    n = len(dict_cnt)
    combis = makeCombination(friends)
    for a, b in combis:
        # 3-1: 선물 기록
        a_cnt = dict_gift[(a,b)] if (a,b) in dict_gift else 0
        b_cnt = dict_gift[(b,a)] if (b,a) in dict_gift else 0
        if a_cnt > b_cnt:
            dict_cnt[a] += 1
            continue
        
        if a_cnt < b_cnt:
            dict_cnt[b] += 1
            continue
        
        # 3-2: 선물 지수
        a_point = dict_friend_point[a] if a in dict_friend_point else 0
        b_point = dict_friend_point[b] if b in dict_friend_point else 0
        if a_point > b_point:
            dict_cnt[a] += 1
            continue
            
        if a_point < b_point:
            dict_cnt[b] += 1
            continue
    
    # 출력
    max_cnt = 0
    for friend in dict_cnt:
        max_cnt = max(max_cnt, dict_cnt[friend])
    return max_cnt