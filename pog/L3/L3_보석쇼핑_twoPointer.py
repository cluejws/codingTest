def solution(gems):
    
    # 계산1: 모든 보석 개수
    cnt = getCount(0, len(gems)-1, gems)

    # 계산2: 출력 편의 위한 0 추가
    gems = [0] + gems
    
    # 계산3: twoPointer / 초기화
    res_arr = []
    
    j = 1
    gem_dict = {}
    gem_dict[gems[j]] = 1
    for i in range(1, len(gems)):
        
        # 계산3-1: 최대길이 얻기
        # 끝 index < len(gem)이면 while 만족하니까 -> 끝index < len(gem) - 1
        while j < len(gems)-1 and len(gem_dict) != cnt:
            
            # (1) 다음 index로 넘어가기
            j += 1
            
            # (2) 다음 index로 dict 반영
            if gems[j] not in gem_dict:
                gem_dict[gems[j]] = 1
            else:
                gem_dict[gems[j]] += 1
                    
        # 계산3-2: 답 후보 추가
        if len(gem_dict) == cnt:
            res_arr.append([i,j])
        else:
            break
        
        # 계산3-3: 다음 i를 위한 제거
        if gem_dict[gems[i]] == 1:
            del gem_dict[gems[i]]
        else:
            gem_dict[gems[i]] -= 1
    
    # 계산4: 정렬
    res_arr.sort(key = lambda x: (x[1]-x[0], x[0]))
    
    return res_arr[0]
        
        
def getCount(i,j, gems):
    
    gem_dict = {}
    for k in range(i,j+1):
        if gems[k] not in gem_dict:
            gem_dict[gems[k]] = 1
            
    return len(gem_dict)