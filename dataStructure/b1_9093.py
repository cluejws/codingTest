num = int(input())

res_list = []
for i in range(0,num):
    line = input()

    # "i " "am" "happy"
    line_list = line.split(" ")

    temp = ""
    for i in range(0,len(line_list)):    
        for j in reversed(range(0,len(line_list[i]))):
            temp += line_list[i][j]
        temp += " "
    
    res_list.append(temp)

for pr in res_list:
    print(pr)      