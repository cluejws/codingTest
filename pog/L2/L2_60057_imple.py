import math

def getResult(s, k):
    
    # 계산1: slice한 리스트 생성
    list_slice = []
    for i in range(0, len(s), k):
        list_slice.append(s[i:i+k])

    # 계산2: res 문자열 생성
    res = ''
    
    cnt = 1
    for i in range(len(list_slice)-1):
        
        # 1. 같으면 res 반영x
        if list_slice[i] == list_slice[i+1]:
            cnt += 1
            continue
        
        # 2. 다르면 res 반영
        if cnt == 1:
            res += list_slice[i]
        else:
            res += (str(cnt) + list_slice[i])
        
        # 3. 다르면 cnt 초기화
        cnt = 1

    # 계산3: 끝 slice 반영
    if cnt == 1:
        res += list_slice[-1]
    else:
        res += (str(cnt) + list_slice[-1])
    
    return len(res)

def solution(s):
    
    # 계산: (1부터 최대 길이)만큼 slice해서 최소 판단 
    min_res = math.inf
    for k in range(1, len(s)+1):
        res = getResult(s, k)
        min_res = min(min_res, res)
    
    return min_res