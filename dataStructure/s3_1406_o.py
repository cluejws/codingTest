# insert = O(N^2)

result_list = list(input())

test_case = int(input())

stack_list = []
for i in range(0,test_case):

    line = input()

    if "L" in line:
        
        if len(result_list) == 0:
            pass
        else:
            stack_list.append(result_list.pop())
    
    elif "D" in line:
        
        if len(stack_list) == 0:
            pass
        else:       
            result_list.append(stack_list.pop())
    
    elif "B" in line:
        
        if len(result_list) == 0:
            pass
        else:
            data = result_list.pop()
    
    elif "P" in line:            
        
        result_list.append(line[2])

res1 = "".join(result_list)
res2 = "".join(reversed(stack_list))

print(res1+res2)