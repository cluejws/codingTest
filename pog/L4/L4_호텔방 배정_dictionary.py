def solution(k, room_number):
    
    res = []
    
    # 계산: 그래프 탐색을 통한 빈방 얻기
    # room_dict[방] = 다음 빈방 / 탐색 후 이전 경로를 다음으로 초기화 
    room_dict = {}
    for i in room_number:
        
        n = i
        visit = [n]
        
        # 계산1: 그래프 탐색을 통해 빈방 찾기
        while n in room_dict:
            n = room_dict[n]
            visit.append(n)
        
        # 계산2: 빈방 추가
        res.append(n)
        
        # 계산3: 이전 경로를 다음(빈방+1)으로 초기화
        for j in visit:
            room_dict[j] = n+1
    
    return res