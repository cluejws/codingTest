num = int(input())

stack_list = []
for i in range(0,num):
    data = int(input())

    if data != 0:
        stack_list.append(data)
    else:
        stack_list.pop()
print(sum(stack_list))
