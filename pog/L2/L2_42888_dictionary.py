def solution(record):
    
    # 계산1: 딕셔너리 생성
    dict_id = {}
    res = []
    for r in record:
        arr = r.split()
        if arr[0] == 'Enter':
            dict_id[arr[1]] = arr[2]
            res.append((arr[0], arr[1]))
        elif arr[0] == 'Leave':
            res.append((arr[0], arr[1]))
        elif arr[0] == 'Change':
            dict_id[arr[1]] = arr[2]
        
    # 계산2: 출력 반영
    print_res = []
    for r in res:
        behavior, id = r
        name = dict_id[id]
        
        if behavior == 'Enter':
            print_res.append(f'{name}님이 들어왔습니다.')
        elif behavior == 'Leave':
            print_res.append(f'{name}님이 나갔습니다.')
         
    return print_res