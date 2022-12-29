def print_arr(n):
    
    # 계산1: 식 구하기
    num_arr = [str(i+1) for i in range(n)]
        
    sum_res = num_arr[0]
    print_res = num_arr[0]
    for i in range(len(arr)):
        if arr[i] == '+':
            sum_res = sum_res + '+' + num_arr[i+1]
            print_res = print_res + '+' + num_arr[i+1]
        elif arr[i] == '-':
            sum_res = sum_res + '-' + num_arr[i+1]
            print_res = print_res + '-' + num_arr[i+1]
        elif arr[i] == ' ':
            sum_res = sum_res + num_arr[i+1]
            print_res = print_res + ' ' + num_arr[i+1]
    
    # 계산2: 계산해서 0 판단
    res = 0
    
    # 계산2-1: sum_res 를 '+'계산하기
    minus_arr = []
    split_arr = sum_res.split('+')
    for sa in split_arr:
        if '-' in sa:
            minus_arr.append(sa)
            continue
        res += int(sa)
    
    # 계산2-2: sum_res 를 '-'계산하기
    minus_res = 0
    for ma in minus_arr:
        split_arr = ma.split('-')
        minus_res += int(split_arr[0])
        for i in range(1, len(split_arr)):
            minus_res -= int(split_arr[i])
    
    # 계산2-3: 총 합 = 0이면 식 출력
    res += minus_res
    if res == 0:
        print(print_res)   
            

def getResult(n, cnt):
    
    # 기저조건: n-1 
    if cnt == n-1:
        print_arr(n)
        return  
    
    # 계산: 백트래킹
    arr.append(' ')
    getResult(n, cnt+1)
    arr.pop()
    
    arr.append('+') 
    getResult(n, cnt+1)
    arr.pop()
    
    arr.append('-')
    getResult(n, cnt+1)
    arr.pop()
    
# 입력
t = int(input())
for _ in range(t):
    
    n = int(input())
    
    arr = []
    getResult(n, 0)
    print()