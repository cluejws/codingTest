def getResult(pb):

    # 계산1: 알파벳 순서 정렬
    pb.sort()

    # 게산2: 1중 반복문(다음 것과 비교)
    n = len(pb)
    for i in range(n-1):

        # 1. 길이
        len_i = len(pb[i])

        # 2. 판단
        is_break = False
        for k in range(len_i):
            if pb[i][k] != pb[i+1][k]:
                is_break = True
                break

        # 3. 판단 후 continue/return 
        if is_break:
            continue
        else:
            return False

    # 계산3: 아무것도 X
    return True

def solution(phone_book):
    res = getResult(phone_book)
    return res