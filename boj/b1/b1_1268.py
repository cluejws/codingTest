num = int(input())

std_list = []
for i in range(0,num):
    student = list(input().split(" "))
    std_list.append(student)

count_list = []
for i in range(0,len(std_list)):
    count_list.append([])

for j in range(0,len(std_list[0])):
    
    for i in range(0,len(std_list)):
        
        for check in range(0,len(std_list)):
            if(std_list[i][j] == std_list[check][j]):
                if check not in count_list[i]:
                    count_list[i].append(check)

max = 0
max_index = 0
for i in range(0,len(std_list)):
    if(max < len(count_list[i])):
        max = len(count_list[i])
        max_index = i
print(max_index+1)    
    