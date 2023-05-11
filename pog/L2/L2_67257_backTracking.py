max_res = 0

def cal(temp, o):
    
    sum_res = -1
    if o == '+':
        sum_res = 0
        for i in range(len(temp)):
            sum_res += temp[i]
    elif o == '-':
        sum_res = temp[0]
        for i in range(1, len(temp)):
            sum_res -= temp[i]
    elif o == '*':
        sum_res = 1
        for i in range(len(temp)):
            sum_res *= temp[i]
    return sum_res

def getResult(arr, expression):
    
    # 1.
    temp1 = expression.split(arr[0])
    
    # 2.
    list_temp1 = []
    for t1 in temp1:
        
        # 1.
        temp2 = t1.split(arr[1])
        
        # 2.
        list_temp2 = []
        for t2 in temp2:
            # 계산
            temp3 = list(map(int, t2.split(arr[2])))
            list_temp2.append(cal(temp3, arr[2]))
        
        # 3.
        list_temp1.append(cal(list_temp2, arr[1]))
    
    # 3.
    return cal(list_temp1, arr[0])
        
def solution(expression):
    
    # 백트래킹
    oper = ['+', '-', '*']
    def backTracking(cnt, expression):
        if cnt == 3:
            res = getResult(arr, expression)
            global max_res
            max_res = max(max_res, abs(res))
            return
        
        for i in range(3):
            if visited[i] == False:
                visited[i] = True
                arr.append(oper[i])
                backTracking(cnt+1, expression)
                arr.pop()
                visited[i] = False
    
    # 계산: 백트래킹
    arr = []
    visited = [False for _ in range(3)]
    backTracking(0, expression)

    global max_res
    return max_res