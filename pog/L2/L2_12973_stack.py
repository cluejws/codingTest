def getResult(s):
    
    # 1. s 순회하면서 stack 판단
    stack = []
    for alp in s:
        if len(stack) > 0 and stack[-1] == alp:
            stack.pop()
        else:
            stack.append(alp)

    # 2. return
    if len(stack) == 0:
        return True
    
    return False
    
def solution(s):
    return (1 if getResult(s) else 0)