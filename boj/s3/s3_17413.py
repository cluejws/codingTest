line = input()

result = ""
temp_list = []
check = False
for i in range(0, len(line)):

    if line[i] == "<":
        if len(temp_list) !=0:
            for j in reversed(range(0,len(temp_list))):
                    result += temp_list[j]

            temp_list = []  

        result += line[i]
        check = True
    elif line[i] == ">":
        result += line[i]
        check = False
    else:
        if check:
            result += line[i]
        else:
            if line[i] != " ":
                temp_list.append(line[i])

                if i == len(line)-1:
                    for j in reversed(range(0,len(temp_list))):
                        result += temp_list[j]
            elif line[i] == " ":
                for j in reversed(range(0,len(temp_list))):
                    result += temp_list[j]
                result += " "
                temp_list = []

print(result)

            

