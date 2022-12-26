num = int(input())

count = 0

for i in range(1, num+1):

    i_break = False
    if i % 2 != 0:

        count_j = 0
        for j in reversed(range(1,i+1)):
            count_j +=1    
            count += 1
            if(count == num):
                str_res1 = j 
                i_break = True
                str_res2 = j + (-i+1) + ((count_j-1) * 2)
                print(f"{str_res1}/{str_res2}")
                break
    else:
        count_j = 0
        for j in range(1, i+1):
            count_j += 1
            count += 1
            if(count == num):
                str_res1 = j
                i_break = True
                str_res2 = j + (i-1) + ((count_j-1) * -2)
                print(f"{str_res1}/{str_res2}")
                break
    if i_break:
        break


