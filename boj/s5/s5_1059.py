length = int(input())

data_list = list(map(int,input().split(" ")))
r_data_list = sorted(data_list)


num = int(input())

start = 0
end = 0
for i in reversed(range(0,len(r_data_list))):
    if num > r_data_list[i]:
        start = r_data_list[i]
        end = r_data_list[i+1]
        break
    else:
        if i == 0:
            start = 0
            end = r_data_list[i]
    

count = 0
for i in range(start+1,end):
    for j in range(i+1, end):
        if i>=j: 
            break
        else:
            temp_start = i
            temp_end = j
            if (i<=num<=j):
                count+=1
print(count)
            
