num = int(input())

# 입력
str_list = []
for i in range(0,num):
    line = input()
    str_list.append(line)


# ?로 바꾸기 
# 비교 없을때 / 비교 있을때
if num == 1:
    print(line)
else:
    
    res_list = []
    for alp in str_list[0]:
        res_list.append(alp)

        
    for i in range(0,len(str_list)):

        for index in range(0,len(str_list[0])):
            if(str_list[i][index] == res_list[index]):
                res_list[index] = str_list[i][index]
            else:
                res_list[index] = "?"
            
    res = ""
    for alp in res_list:
        res += alp
    print(res)     

    


