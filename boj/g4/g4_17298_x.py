import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int,input().split(" ")))

for i in range(n):
    
    max_num = -1
    for j in range(i,n):
        if arr[i] < arr[j]:
            max_num = arr[j]
            is_break = True
            break
    print(max_num , end=" ")
    
        
