def getResult(n, losts, reserves):
    
    # 계산1: 정렬
    losts.sort()
    reserves.sort()
    
    # 계산2: 같은 것 제거(reserves, losts)
    for reserve in reserves[:]:
        if reserve in losts:
            losts.remove(reserve)
            reserves.remove(reserve)

    # 계산3: reserve의 왼쪽, 오른쪽 순으로 제거(losts)
    for reserve in reserves[:]:
        if (reserve - 1) in losts:
            losts.remove(reserve-1)
        elif (reserve + 1) in losts:
            losts.remove(reserve+1)

    return n - len(losts)
              
def solution(n, lost, reserve):
    return getResult(n, lost, reserve)