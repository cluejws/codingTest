from collections import deque

def getResult(people, limit):
    
    # 계산1: 내림차순 정렬
    people.sort(reverse=True)
    
    # 계산2: deque이용
    # 합 limit보다 작거나 같으면 양쪽 빼기
    # 합 limit보다 크면 가장 큰 것 빼기
    
    # 1. 1개 또는 0개 까지 반영
    d = deque(people)
    cnt = 0
    while len(d) >= 2:
        front = d.popleft()
        back = d.pop()
        
        if front + back <= limit:
            cnt += 1
        else:
            cnt += 1
            d.append(back)
    
    # 2. 1개 판단 후 반영
    if len(d) == 1:
        cnt += 1

    return cnt
        
def solution(people, limit):
    return getResult(people, limit)