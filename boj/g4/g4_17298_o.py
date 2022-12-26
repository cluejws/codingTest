# 입력
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split(" ")))
stack_list = [(arr[0],0)] # (값,인덱스)
nge_list = [-1 for _ in range(n)]

# 계산
for i in range(1,n):
    
    if stack_list[-1][0] >= arr[i]:
        stack_list.append((arr[i],i))
    else:
        while len(stack_list) !=0 :
            if stack_list[-1][0] < arr[i]:
                nge_list[stack_list[-1][1]] = arr[i]
                data = stack_list.pop()
            else:
                break
        stack_list.append((arr[i],i))

# 출력
nge_list = list(map(str,nge_list))
print(" ".join(nge_list))
