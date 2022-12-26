def push(data):
    queue_list.append(data)

def pop():
    if len(queue_list) == 0:
        return -1
    else:
        data = queue_list.pop(0)
        return data

def size():
    return len(queue_list)

def empty():
    if len(queue_list) == 0 :
        return 1
    else:
        return 0

def front():
    if len(queue_list) == 0:
        return -1
    else:
        return queue_list[0]

def back():
    if len(queue_list) == 0:
        return -1
    else:
        return queue_list[-1]

num = int(input())

queue_list = []
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
    elif "front" in line:
        print_list.append(front())
    elif "back" in line:
        print_list.append(back())

for pr in print_list:
    print(pr)