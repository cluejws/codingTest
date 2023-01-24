def getD(n):

    n = n * 2
    if n > 9999:
        return n % 10000
    
    return n

def getS(n):
    
    n = n - 1
    if n < 0:
        return 9999
    
    return n

def getL(n):
    
    str_n = str(n)
    len_str_n = len(str_n)
    str_n = '0' * (4 - len_str_n) + str_n
    
    temp_str_n = str_n[1:4] + str_n[0]
    return int(temp_str_n)
    
def getR(n):
    
    str_n = str(n)
    len_str_n = len(str_n)
    str_n = '0' * (4 - len_str_n) + str_n
    
    temp_str_n = str_n[-1] + str_n[0:3]
    return int(temp_str_n)
    

def getResult(a,b):
    
    visited = [-1 for _ in range(10000)]
    queue = deque()
    
    queue.append((a, ''))
    visited[a] = len('')
    
    while len(queue) != 0:
        
        cur_num, cur_str = queue.popleft()
        if cur_num == b:
            return cur_str
        
        d = getD(cur_num)
        next_str = cur_str + 'D'
        if visited[d] == -1:
            queue.append((d, next_str))
            visited[d] = len(next_str)

            
        s = getS(cur_num)
        next_str = cur_str + 'S'
        if visited[s] == -1:
            queue.append((s, next_str))
            visited[s] = len(next_str)

            
        l = getL(cur_num)
        next_str = cur_str + 'L'
        if visited[l] == -1:
            queue.append((l, next_str))
            visited[l] = len(next_str)

            
        r = getR(cur_num)
        next_str = cur_str + 'R'
        if visited[r] == -1:
            queue.append((r, next_str))
            visited[r] = len(next_str)

        
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    a,b = map(int,input().split())
    res = getResult(a,b)
    print(res)
