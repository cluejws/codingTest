import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    # 입력
    w = input().rstrip()
    k = int(input())
    
    # 계산1: 딕셔너리 만들기 
    dict_w = {}
    for i in range(len(w)):
        if w[i] in dict_w:
            dict_w[w[i]].append(i)
        else:
            dict_w[w[i]] = [i]
            
    # 계산2: sliding window
    # 3번게임 -> 시작,끝 같을 때 최소 차이
    # 4번게임 -> 시작,끝 같을 때 최대 차이
    min_res = math.inf
    max_res = 0
    
    for key in dict_w:
        value = dict_w[key]
        
        if len(value) < k:
            continue
        
        for i in range(0, len(value) - k + 1):
            sum_res = value[i+k-1] - value[i] + 1
            min_res = min(min_res, sum_res)
            max_res = max(max_res, sum_res)
    
    # 출력
    if min_res == math.inf or max_res == 0:
        print(-1)
    else:
        print(min_res, max_res)