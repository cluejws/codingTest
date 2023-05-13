import math

def solution(gems):
    
    # 계산1: gems 후보 개수 얻기
    set_gems = set(gems)
    k = len(set_gems)
    
    # 계산2: twoPointer
    n = len(gems)
    min_res = math.inf
    res = []
    
    j = 0
    dict_gems = {}
    dict_gems[gems[j]] = 1
    for i in range(n):

        # 1.
        while j + 1 < n and len(dict_gems) < k:
            if gems[j + 1] in dict_gems:
                dict_gems[gems[j + 1]] += 1
            else:
                dict_gems[gems[j + 1]] = 1
            
            j += 1
            
        # 2.
        if len(dict_gems) < k:
            break
           
        # 3.
        if min_res > (j - i + 1):
            min_res = (j - i + 1)
            res = [i+1, j+1]
        
        # 4.
        if dict_gems[gems[i]] > 1:
            dict_gems[gems[i]] -= 1
        else:
            del dict_gems[gems[i]] 
        
    return res