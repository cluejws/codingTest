from collections import deque

num = int(input())

num_queue = deque([i for i in range(1,num+1)])

while 1:

    if len(num_queue) == 1:
        break

    num_queue.popleft()
    temp = num_queue.popleft()
    num_queue.append(temp)
    


print(num_queue[0])