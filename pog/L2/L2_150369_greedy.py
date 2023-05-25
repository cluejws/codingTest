def solution(cap, n, deliveries, pickups):
    
    # 계산1: 뒤집기
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    
    # 계산2: 
    # 해당 위치 반영 
    # 해당 위치 최대로 배달/수거(양수 아닐 때까지)
    have_to_deli = 0
    have_to_pick = 0
    
    min_dist = 0
    for i in range(n):
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]
        
        while have_to_deli > 0 or have_to_pick > 0:
            have_to_deli -= cap
            have_to_pick -= cap
            min_dist += (n - i) * 2

    return min_dist