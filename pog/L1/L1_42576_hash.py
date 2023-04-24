def getResult(participant, completion):
    
    # 1. 딕셔너리 생성
    dict_participant = {}
    for pa in participant:
        if pa in dict_participant:
            dict_participant[pa] += 1
        else:
            dict_participant[pa] = 1
    
    # 2. 방문처리
    for co in completion:
        dict_participant[co] -= 1
    
    # 3. 0이 아닌수 판단
    for pa in dict_participant:
        if dict_participant[pa] > 0:
            return pa

def solution(participant, completion):
    res = getResult(participant, completion)
    return res