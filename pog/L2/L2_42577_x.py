def check(i,j, pb):
    len_i = len(pb[i])
    for k in range(len_i):
        if pb[i][k] != pb[j][k]:
            return False
        
    return True

def getResult(pb):
    
    # 1. 길이 정렬
    pb.sort(key=lambda x: len(x))
    
    # 2. 2중 반복문
    n = len(pb)
    for i in range(n):
        for j in range(i+1, n):
            if check(i,j, pb):
                return False
            
    return True
            
def solution(phone_book):
    res = getResult(phone_book)
    return res