num = int(input())

res_list = [64]
while True:

    sum = 0
    for i in range(0,len(res_list)):
        sum += res_list[i]

    if sum > num:

        min = int(res_list[-1] / 2)
        
        temp_list = []
        for i in range(0, len(res_list)-1): 
            temp_list.append(res_list[i])
        temp_list.append(min)

        temp_sum = 0
        for i in range(0, len(temp_list)):
            temp_sum += temp_list[i]
        
        if temp_sum >= num:
            res_list = temp_list
        else: 
            temp_list.append(min)
            res_list = temp_list
            
    elif sum == num:
        print(len(res_list))
        break
    