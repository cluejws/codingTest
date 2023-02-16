def check(begin, cur):
    
    # 계산1: 차이 수 계산
    differ_cnt = 0
    for i in range(len(begin)):
        if begin[i] != cur[i]:
            differ_cnt += 1
    
    # 계산2: 차이 수 0,1 경우 진행
    if differ_cnt == 0:
        return True
    elif differ_cnt == 1:
        return True
    
    return False

def solution(begin, target, words):
    
    # 재귀 함수 선언
    def dfs(begin, target, cnt):
    
        # 기저조건: 같으면 최소값 할당
        if begin == target:
            global res
            res = min(res, cnt)
            return
            
        for i in range(len(words)):
            cur = words[i]
            if check(begin, cur) and visited[i] == False:
                visited[i] = True
                dfs(cur, target, cnt+1)
                visited[i] = False
    
    # 계산: 재귀
    visited = [False for _ in range(len(words))]
    dfs(begin, target, 0)
    
    # 출력
    global res
    if res == math.inf:
        return 0
    else:
        return res

import math
res = math.inf