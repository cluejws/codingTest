def push(data):
    result_list.append(data)

def pop():
    
    if len(result_list) == 0:
        res = -1
    else:
        res = result_list.pop()

    return res

def size():
    return len(result_list)

def empty():
    
    if len(result_list) == 0:
        res = 1
    else:
        res = 0

    return res

def top():
    
    if len(result_list) == 0:
        res = -1
    else:
        res = result_list[-1]

    return res

num = int(input())

result_list = []
print_list = []
for i in range(0,num):
    line = input()

    if "push" in line :
        temp_list = line.split(" ")
        push(int(temp_list[-1]))
    elif "pop" in line:
        print_list.append(pop())
    elif "size" in line:
        print_list.append(size())
    elif "empty" in line:
        print_list.append(empty())
    elif "top" in line:
        print_list.append(top())

for pr in print_list:
    print(pr)