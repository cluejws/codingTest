int_list = list(map(int,input().split(" ")))

data_list =  list(i for i in range(1,int_list[0]+1)) 


count = int_list[1] - 1
count_list = [count]
res_list = [data_list[count]]

for i in range(0,int_list[0]-1 ):

    for i in range(0,int_list[1]):
        count = (count + 1 ) % int_list[0]
        while True:
            if count in count_list:
                count = (count + 1) % int_list[0]
            else:
                break
    
    count_list.append(count)
    res_list.append(data_list[count])

print("<"+(", ").join(map(str,res_list))+">")


