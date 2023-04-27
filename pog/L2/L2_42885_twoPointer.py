def getResult(people, limit):
    
    # 계산1: 내림차순 정렬
    people.sort(reverse=True)
    
    # 계산2: twoPointer
    # 합 limit보다 작거나 같으면 양쪽 빼기
    # 합 limit보다 크면 가장 큰 것 빼기
    left = 0
    right = len(people) - 1
    
    cnt = 0
    while left <= right:
        if (people[left] + people[right]) > limit:
            left += 1
            cnt += 1
        else:
            left += 1
            right -= 1
            cnt += 1
            
    return cnt
        
def solution(people, limit):
    return getResult(people, limit)