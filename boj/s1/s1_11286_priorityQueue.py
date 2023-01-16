import heapq, sys
input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    
    line = int(input())
    
    # 0 입력O
    if line == 0:
        
        if len(arr) == 0:
            print(0)
            continue
        
        abs_val, val = heapq.heappop(arr)
        print(val)
    
    # 0 입력X
    else:
        heapq.heappush(arr, (abs(line), line))