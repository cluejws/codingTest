def getTupleList(s):
    slice_str = s[2:len(s)-2]
    str_list = slice_str.split('},{')

    tp_list = []
    for tp_str in str_list:
        tp_list.append(list(map(int,tp_str.split(','))))

    return tp_list

def solution(s):
    answer = []
    
    # 계산1: tuple list 얻기
    tp_list = getTupleList(s)
    
    # 계산2: tuple을 길이로 정렬
    tp_list.sort(key = lambda tp: (len(tp)))
    
    # 계산3: tuple을 딕셔너리로 중복 판단
    dict_tp = {}
    for tp in tp_list:
        for i in tp:
            if i not in dict_tp:
                dict_tp[i] = 1
                answer.append(i)
        
    return answer