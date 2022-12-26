num = int(input())

print_list = []
for i in range(0,num):
    
    data_list = list(map(int,input().split(" ")))
    
    sum = 0
    for j in range(0, data_list[0]):
        sum += data_list[j+1]
    avg = sum / data_list[0]

    count = 0
    for j in range(0,data_list[0]):
        if float(data_list[j+1]) > avg:
            count += 1

    res = str(round(float(count/data_list[0] * 100.0),3))

    search = 0
    for j in range(0,len(res)):
        if res[j] == ".":
            search = j+1
    
    if len(res)-1 - search == 2:
        res += "%"
    elif len(res)-1 - search ==1:
        res += "0%"
    elif len(res)-1 - search ==0:
        res += "00%"

    print_list.append(res)
        
for pr in print_list:
    print(pr)