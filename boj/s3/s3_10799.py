data_list = list(input())

stack_list = []
count = 0

for i in range(0, len(data_list)):
    if data_list[i] == "(":
        stack_list.append(data_list[i])
    
    else:
        if data_list[i-1] == "(":
            stack_list.pop()
            count = count + len(stack_list)
        else:
            stack_list.pop()
            count = count + 1

print(count)