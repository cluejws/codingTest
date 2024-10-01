def set_fm(fm, num):
    # 기저조건
    if num == 0:
        return '0'

    # 계산: 진법
    arr = []
    while num != 0:
        arr.append(num % fm)
        num = num // fm

    return ''.join(map(str, arr[::-1]))

def calculate_fm(fm, num_str):
    num = 0
    for idx, value in enumerate(num_str[::-1]):
        num += (fm ** idx) * int(value)
    
    return num
    
def isPlus(fm, a_str, b_str, c_str):
    # 1.
    num_a = calculate_fm(fm, a_str)
    num_b = calculate_fm(fm, b_str)
    num_c = calculate_fm(fm, c_str)
    
    # 2.
    if (num_a + num_b) == num_c:
        return True
    
    return False

def isMinus(fm, a_str, b_str, c_str):
    # 1.
    num_a = calculate_fm(fm, a_str)
    num_b = calculate_fm(fm, b_str)
    num_c = calculate_fm(fm, c_str)
    
    # 2.
    if (num_a - num_b) == num_c:
        return True
    
    return False

def check(fm, num_str):
    for ele in num_str:
        if int(ele) >= fm:
            return False
        
    return True

def solution(expressions):
    # 1. 가능 진법(진수 범위 내 판단)
    fm1_set = set([2,3,4,5,6,7,8,9])
    for expression in expressions:
        
        # 1-1
        temp = expression.split()
        
        # 1-2
        for fm in range(2, 9+1):
            if temp[-1] == 'X':
                if not(check(fm, temp[0]) and check(fm, temp[2])):
                    if fm in fm1_set: 
                        fm1_set.remove(fm)
            else:
                if not(check(fm, temp[0]) and check(fm, temp[2]) and check(fm, temp[4])):
                    if fm in fm1_set:
                        fm1_set.remove(fm)

    # 2. 가능 진법(진수 계산 판단)
    fm2_set = set(list(fm1_set))
    for expression in expressions:
        
        # 2-1
        temp = expression.split()
        if temp[-1] == 'X':
            continue
        
        # 2-2
        for fm in fm1_set:
            if temp[1] == '+':
                if not isPlus(fm, temp[0], temp[2], temp[4]) and fm in fm2_set: 
                        fm2_set.remove(fm)
            elif temp[1] == '-':
                if not isMinus(fm, temp[0], temp[2], temp[4]) and fm in fm2_set: 
                        fm2_set.remove(fm)
                
    # 출력
    answers = []
    for expression in expressions:
        
        # 1. 기저조건
        temp = expression.split()
        if temp[-1] != 'X':
            continue
            
        # 2. 중복제거
        res_set = set()
        for fm in fm2_set:
            # 2-1: 계산
            num_a = calculate_fm(fm, temp[0])
            num_b = calculate_fm(fm, temp[2])
            if temp[1] == '+':
                res = set_fm(fm, num_a + num_b)
                res_set.add(res)
            elif temp[1] == '-':
                res = set_fm(fm, num_a - num_b)
                res_set.add(res)
                
        # 3. 출력
        answer = temp[:]
        answer.pop()
        if len(res_set) > 1:
            answer.append('?')
        else:
            for res in res_set:
                answer.append(res)
        
        answers.append(' '.join(answer))
        
    return answers