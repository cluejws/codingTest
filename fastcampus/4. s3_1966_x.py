num = int(input()) #테스트 케이스
print_list = []

for i in range(0,num):
    list_int1 = list(map(int,input().split(" "))) # 문서수, 현재queue에 몇번째로 있는지
    list_int2 = list(map(int,input().split(" "))) # 중요도/ 중요도가 클수록 먼저 출력

    # 딕셔너리를 통해 키: 중요도 / 값: 개수
    dict_i = {}
    
    for data in list_int2:
        
        list_keys = list(dict_i.keys())
        
        if data in list_keys:
            value = dict_i[data]
            value += 1
            dict_i[data] = value
        else:
            dict_i[data] = 1 

    rank = 1
    find_data = list_int2[list_int1[1]]

    for data in list_int2:
        if(find_data <= data):
            rank += 1
    
    list_keys = list(dict_i.keys())
    for key in list_keys:
        if(dict_i[key] > 1):
            rank -= 1

    print_list.append(rank-1)

for pr in print_list:
    print(pr)

  
    
       

    

