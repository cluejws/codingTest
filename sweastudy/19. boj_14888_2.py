def getResult(cnt,sum): #cnt: 연산넣은개수, sum: 지금까지 더한값
    
    
    #1. 기저조건: 할당
    global min_res, max_res
    if cnt == n-1:
           
        if sum > max_res:
            max_res = sum
        
        if sum < min_res:
            min_res = sum  
        return  
            
    #2. 재귀    
    if cal_num_arr[0] > 0:   #덧셈
        
        cal_num_arr[0] -= 1
        getResult(cnt+1, sum + num_arr[cnt+1])
        cal_num_arr[0] += 1
        
    if cal_num_arr[1] > 0: #뺄셈
        
        cal_num_arr[1] -= 1
        getResult(cnt+1, sum - num_arr[cnt+1])
        cal_num_arr[1] += 1
        
    if cal_num_arr[2] > 0: #곱셈
        
        cal_num_arr[2] -= 1
        getResult(cnt+1, sum * num_arr[cnt+1])
        cal_num_arr[2] += 1
        
    if cal_num_arr[3] > 0: #나눗셈
        
        cal_num_arr[3] -= 1
        
        if sum >= 0:
            getResult(cnt+1, sum // num_arr[cnt+1])
        else: 
            temp = -sum    
            temp = temp // num_arr[cnt+1]
            getResult(cnt+1, -temp)
    
        cal_num_arr[3] += 1
            
# 입력
import math

n = int(input())
num_arr = list(map(int,input().split()))
cal_num_arr = list(map(int,input().split()))

# 계산
min_res = math.inf
max_res = -math.inf
res = [0 for _ in range(n-1)] 
getResult(0,num_arr[0])

# 출력
print(max_res)
print(min_res)