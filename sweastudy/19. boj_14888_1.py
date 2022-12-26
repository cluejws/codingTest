def getResult(cnt,arr): #cnt: 연산넣은개수, arr: cal_arr의 인덱스값(반복없는 순열위함)
    
    
    #1. 기저조건 할당
    global min_res, max_res
    if cnt == n-1:
    
        # 계산 1: 합 구하기
        sum = num_arr[0]
        for i in range(len(arr)):
            if cal_arr[arr[i]] == '+':

                sum += num_arr[i+1]
            elif cal_arr[arr[i]] == '-':

                sum -= num_arr[i+1] 
            elif cal_arr[arr[i]] == '*':

                sum *= num_arr[i+1]
            else:

                if sum >= 0:
                    sum = sum // num_arr[i+1]
                else:
                    temp = -sum
                    temp = temp // num_arr[i+1]
                    sum = -temp 
        
        # 계산2: 최대 & 최소 판별       
        if sum > max_res:
            max_res = sum
        
        if sum < min_res:
            min_res = sum  
        return  
            
    #2. 재귀
    for i in range(n-1):
        if i not in arr:
            arr.append(i)
            getResult(cnt+1, arr)
            arr.pop()
            
# 입력
import math

n = int(input())
num_arr = list(map(int,input().split()))
cal_num_arr = list(map(int,input().split()))

cal_arr = []
for i in range(len(cal_num_arr)):
    if i == 0:
        for _ in range(cal_num_arr[i]):
            cal_arr.append('+')
    elif i == 1:
        for _ in range(cal_num_arr[i]):
            cal_arr.append('-')
    elif i == 2:
        for _ in range(cal_num_arr[i]):
            cal_arr.append('*')
    else:
        for _ in range(cal_num_arr[i]):
            cal_arr.append('/')
# 계산
min_res = math.inf
max_res = -math.inf
res = [0 for _ in range(n-1)] 
getResult(0,[])

# 출력
print(max_res)
print(min_res)