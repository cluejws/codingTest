from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    # 입력
    p = list(input().strip())
    n = int(input())
    arr = deque(input().strip()[1:-1].split(','))
    
    # 계산1: arr가 ['']일때를 방지
    if n == 0:
        arr = deque([])
    
    # 계산2: 연산 계산
    break_flag = False
    reverse_cnt = 0
    for line in p:
        if line == 'R':
            reverse_cnt += 1
        
        elif line == 'D':
            
            if len(arr) == 0:
                print('error')
                break_flag = True
                break
            else:
                if reverse_cnt % 2 == 1:
                    arr.pop()
                else:
                    arr.popleft()

    # 계산3: 뒤집기 연산 후 출력
    if not break_flag:
        if reverse_cnt % 2 == 1:
            sorted_arr = list(arr)
            sorted_arr.reverse()
            
            print("[", end = "")
            print(",".join(sorted_arr), end = "")
            print("]")

        else:
            sorted_arr = list(arr)

            print("[", end = "")
            print(",".join(sorted_arr), end = "")
            print("]")