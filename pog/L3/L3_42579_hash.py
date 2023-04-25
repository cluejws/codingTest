import heapq

def getDict(genres,plays):
    dict_genre = {}
    dict_cnt = {}
    
    n = len(genres)
    for i in range(n):
        genre = genres[i]
        if genre in dict_genre:
            dict_genre[genre].append((plays[i], i))
            dict_cnt[genre] += plays[i]
        else:
            dict_genre[genre] = [(plays[i], i)]
            dict_cnt[genre] = plays[i]
    
    return dict_genre, dict_cnt
       
def getResult(genres, plays):
    
    # 계산1: 딕셔너리 생성
    dict_genre, dict_cnt = getDict(genres,plays)
    
    # 계산2: 우선순위큐 생성(가장 많이 재생 장르)
    heap = []
    for genre in dict_cnt:
        heapq.heappush(heap, (-dict_cnt[genre], genre))
        
    # 계산3: res 생성
    res = []
    while len(heap) > 0:
        
        # 1. 최대 재생 장르 / 정렬 반대(재생 수 낮은 순, 고유 번호 높은 순)
        sum_play, genre = heapq.heappop(heap)
        list_cnt = dict_genre[genre]
        list_cnt.sort(key=lambda x: (x[0], -x[1]))        
        
        # 2. 최대 재생 장르 중 노래 2개
        cnt = 0
        for _ in range(len(list_cnt)):
            if cnt == 2:
                break
                
            play, i = list_cnt.pop()
            res.append(i)
            cnt += 1
    
    return res
    
def solution(genres, plays):
    res = getResult(genres, plays)
    return res