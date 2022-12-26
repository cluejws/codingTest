class listDeque:
    def __init__(self):
        self.list_deque = []
    def push_front(self, x):
        self.list_deque.insert(0,x)
    def push_back(self,x):
        self.list_deque.append(x)
    def pop_front(self):
        if len(self.list_deque) == 0:
            return -1
        return self.list_deque.pop(0)
    def pop_back(self):
        if len(self.list_deque) == 0:
            return -1
        return self.list_deque.pop() 
    def size(self):
        return len(self.list_deque)
    def empty(self):
        if len(self.list_deque) == 0:
            return 1
        else:
            return 0
    def front(self):
        if len(self.list_deque) == 0:
            return -1
        return self.list_deque[0]
    def back(self):
        if len(self.list_deque) == 0:
            return -1
        return self.list_deque[-1]
    

import sys
input = sys.stdin.readline

t = int(input())
lq = listDeque()

for _ in range(t):
    t_case = input().split()
    if len(t_case) == 1:
        if t_case[0] == "pop_front":
            print(lq.pop_front())
        elif t_case[0] == "pop_back":
            print(lq.pop_back())
        elif t_case[0] == "size":
            print(lq.size())
        elif t_case[0] == "empty":
            print(lq.empty())
        elif t_case[0] == "front":
            print(lq.front())
        elif t_case[0] == "back":
            print(lq.back())
        else:
            print("오류")
    elif len(t_case) == 2:
        if t_case[0] == "push_front":
            lq.push_front(t_case[1])
        elif t_case[0] == "push_back":
            lq.push_back(t_case[1])
        else:
            print("오류")          