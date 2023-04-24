def getResult(nums):
    
    # 1. 중복제거
    set_nums = set(nums)
    
    # 2. 개수 세기
    n = len(nums)
    
    # 3. 1/2개 했을때 판단
    if len(set_nums) >= (n // 2):
        return n // 2
    else:
        return len(set_nums)

def solution(nums):
    res = getResult(nums)
    return res