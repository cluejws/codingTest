num = int(input())

for i in range(0,num):
    line = input()

    stack_list = []
    stack_list2 = []
    for alp in line:
        if alp == "<":
            if len(stack_list) == 0:
                pass
            else:
                data = stack_list.pop()
                stack_list2.append(data)
        elif alp == ">":
            if len(stack_list2) == 0:
                pass
            else:
                data = stack_list2.pop()
                stack_list.append(data)
        elif alp == "-":
                if len(stack_list) != 0:
                    stack_list.pop()
                else:
                    pass
        else:
            stack_list.append(alp)
        
    print("".join(stack_list) + "".join(reversed(stack_list2)))
