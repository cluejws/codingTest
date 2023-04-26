def getResult(s):
    
    list_alp = []
    for alp in s:
        if alp == '(':
            list_alp.append('(')
        elif alp == ')':
            if len(list_alp) > 0:
                list_alp.pop()
            elif len(list_alp) == 0:
                return False
            
    if len(list_alp) > 0:
        return False
    
    return True

def solution(s):
    res = getResult(s)
    return res