def solution(players, callings):
    
    # 계산1: 해쉬 생성
    dict_player = {}
    dict_rank = {}
    for i, v in enumerate(players):
        dict_player[v] = i+1
        dict_rank[i+1] = v
    
    # 계산2: callings 순회
    for call in callings:
        
        # 1. player 얻기
        rank = dict_player[call]
        ch_player = dict_rank[rank-1]
        
        # 2. 순서 바꾸기(빠름)
        dict_player[ch_player] += 1
        dict_rank[rank] = ch_player
        
        dict_player[call] = rank-1
        dict_rank[rank-1] = call 
        
        
    # 계산3: 배열화 후 정렬
    arr = []
    for player in dict_player:
        rank = dict_player[player]
        arr.append((rank, player))
    
    arr.sort()

    # return
    answer = []
    for a in arr:    
        answer.append(a[1])
    return answer
