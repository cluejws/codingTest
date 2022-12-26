import sys
input = sys.stdin.readline

N, K = map(int,input().split())
arr = [i for i in range(1,N+1)] 
print_arr= []

index = 0
for i in range(N):
    index += (K-1)
    
    if index >= len(arr):
        index %= len(arr)
    
    print_arr.append(str(arr[index]))
    
    arr.pop(index)

print("<",', '.join(print_arr),">", sep="")