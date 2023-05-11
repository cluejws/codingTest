def check(x):
    if 65 <= ord(x) <= 90:
        return True
    return False

def getSet(strInput):
    
    dict_str = {}
    for i in range(len(strInput)-1):

        # 알파벳 대문자 check
        if check(strInput[i].upper()) and check(strInput[i+1].upper()):
            temp = strInput[i].upper() + strInput[i+1].upper()
            if temp in dict_str:
                dict_str[temp] += 1
            else:
                dict_str[temp] = 1
    return dict_str
                
def solution(str1, str2):        
    
    # 1. 해쉬(중복포함)
    set1 = getSet(str1)
    set2 = getSet(str2)
    
    # 2. 교집합, 합집합 구하기
    inter = []
    for s1 in set1:
        if s1 in set2:
            min_s = min(set1[s1], set2[s1])
            for _ in range(min_s):
                inter.append(s1)
                
    union = []
    for s1 in set1:
        if s1 in set2:
            max_s = max(set1[s1], set2[s1])
            for _ in range(max_s):
                union.append(s1)
        else:
            for _ in range(set1[s1]):
                union.append(s1)
    
    for s2 in set2:
        if s2 not in set1:
            for _ in range(set2[s2]):
                union.append(s2)
            
    # 3. 유사도 구하기
    if len(inter) == 0 and len(union) == 0:
        return 1 * 65536
    
    return int((len(inter) / len(union)) * (65536))
