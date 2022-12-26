int_list = list(map(int,input().split(" "))) # 1:줄 수(i) 2:몇 글자(j)

# 받은 체스판 배열로 저장하기
arr = []
for i in range(0,int_list[0]):
    
    data = input()

    arr.append([])
    for alp in data:
        arr[i].append(alp)        

count_list = []
for iter_i in range(0,int_list[0]-7):
    for iter_j in range(0,int_list[1]-7):
        
        # 8*8 짜르기
        temp_arr = []
        cnt_i = 0
        for i in range(iter_i,iter_i+8):
            
            temp_arr.append([])

            cnt_j = 0
            for j in range(iter_j,iter_j+8):
                temp_arr[cnt_i].append(arr[i][j])
                cnt_j += 1                
            
            cnt_i += 1
        
        # 짜른 temp_arr로 판단
        # W로 시작할때로 고정시키고 변경되는 횟수와 
        # B로 시작할때로 고정시키고 변경되는 횟수로 비교
        index1 =0
        index2 =0
        for i in range(0,8):
            for j in range(0,8):
                if (i+j) % 2 == 0:
                    if temp_arr[i][j] != 'W': #W로 시작할때 작동
                        index1 += 1
                    if temp_arr[i][j] != 'B': #B로 시작할때 작동
                        index2 += 1
                else:
                    if temp_arr[i][j] != 'B': #W로 시작할때 작동
                        index1 += 1
                    if temp_arr[i][j] != 'W': #B로 시작할때 작동
                        index2 += 1

        count_list.append(min(index1,index2))

print(min(count_list))