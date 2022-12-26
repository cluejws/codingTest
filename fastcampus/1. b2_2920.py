temp_list = []
int_list = list(map(int,input().split(" ")))

for i in range(0,7):
    temp_list.append(int_list[i+1]- int_list[i])

for i in range(0,7):

    if(temp_list[i] != 1 and temp_list[i] != -1):
        print("mixed")
        break
    
    if(i == 6):
        if(temp_list[i]==1):
            print("ascending")
        elif(temp_list[i]==-1):
            print("descending")
