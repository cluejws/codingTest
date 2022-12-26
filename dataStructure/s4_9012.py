num = int(input())

print_list = []
for i in range(0,num):
    
    line = input() 
    stack_list = []
    
    is_pass = False
    for data in line:
        
        if data == "(":
            stack_list.append(data)
        elif data ==")":
            if len(stack_list) == 0:
                print_list.append("NO")
                is_pass = True
                break
            else:
                stack_list.pop()
    
    if is_pass:  # 끝까지 도달하기전에 만족x   
        pass
    else:
        if len(stack_list) == 0:  # 끝까지 도달했는데 만족
            print_list.append("YES")
      
        else:   # 끝까지 도달했는데 만족x
            print_list.append("NO")

for pr in print_list:
    print(pr)
        
        