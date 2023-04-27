def getResult(number, k):
    
    # 계산1: 빼기
    cnt = 0
    stack = []
    id = -1
    for i in range(len(number)):
        
        while len(stack) > 0 and int(stack[-1]) < int(number[i]) and cnt < k:
            stack.pop()
            cnt += 1
        
        stack.append(number[i])
        
    # 계산2: k 만큼 안뺄 경우
    if cnt == k:
        return ''.join(stack)
    else:
        diff = k - cnt
        for _ in range(diff):
            stack.pop()
        return ''.join(stack)

def solution(number, k):
    return getResult(number, k)