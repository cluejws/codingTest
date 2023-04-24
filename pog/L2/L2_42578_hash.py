def solution(clothes):
    
    # 1. 딕셔너리 생성
    dict_cloth = {}
    for cloth in clothes:
        name, kind = cloth
        if kind in dict_cloth:
            dict_cloth[kind].append(name)
        else:
            dict_cloth[kind] = [name]
    
    # 2. 개수 list 생성
    cnt_kind = []
    for kind in dict_cloth:
       cnt_kind.append(len(dict_cloth[kind])) 
    
    # 3. (개수1o+개수1x) * (..) - 1
    sum_res = 1
    for cnt in cnt_kind:
        sum_res *= (cnt+1)
    sum_res -= 1
    
    return sum_res