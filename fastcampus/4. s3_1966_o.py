num = int(input()) # 입력(테스트 케이스 개수)
print_list = []

for i in range(0,num):
    list_int1 = list(map(int,input().split(" "))) # 입력(문서수, 현재queue에 몇번째로 있는지)
    list_int2 = list(map(int,input().split(" "))) # 입력(중요도 : 중요도가 클수록 먼저 출력)
    
# ---------------------------------------------------------------------------------------------- #
    # (위치, 중요도) tuple 배열 만들기
    list_tuple = []
    for index, data in enumerate(list_int2):
        list_tuple.append((index,data))

    find_tuple = list_tuple[list_int1[1]] # 찾고자 하는 tuple
    pop_tuple = (0,0) # 출력 했을때 tuple
    count = 0

    # 출력 할 만큼
    for x in range(len(list_int2)):
        
        # 최대 중요도 tuple찾기(큰 중요도만 찾기, 같은 중요도는 그 자체로 두기)
        max_tuple = (0,0)
        for tup in list_tuple:
            if tup[1] > max_tuple[1]:
                max_tuple = tup
        
        # tuple 배열 내에서 위치 바꾸기
        for y in range(len(list_int2)):
            
            if(list_tuple[0] != max_tuple):
               data = list_tuple.pop(0)
               list_tuple.append(data)
            else:
               pop_tuple = list_tuple.pop(0)
               count +=1
               break 
        
        # 만약 찾고자 하는 tuple = 출력 했을때 tuple 끝
        if(pop_tuple == find_tuple):
            print_list.append(count)
            break

for pr in print_list:
    print(pr)
        
        

    


    
        
