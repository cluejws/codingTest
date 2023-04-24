def getResult(phone_book):
    
    # 1. 딕셔너리 생성
    dict_pb = {}
    for pb in phone_book:
        dict_pb[pb] = 1
        
    # 2. 딕셔너리 key 순회
    # key 쪼개서 존재하는지 판단
    for pb in phone_book:
        temp = ''
        for p in pb:
            temp += p
            if temp in dict_pb and temp != pb:
                return False
    
    return True

def solution(phone_book):
    res = getResult(phone_book)
    return res