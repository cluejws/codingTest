# 입력
import sys
input = sys.stdin.readline

list_line = input().rstrip()

# 계산0: 길이 계산
n = len(list_line)

# 계산1: greedy
list_res = ['X' for _ in range(n)]
cnt = 0
for i in range(n):
    
    # 1. X 경우
    # -> 4개 경우 할당
    if list_line[i] == 'X':
        cnt += 1
        if cnt == 4:
            list_res[i-3: i+1] = 'AAAA'
            cnt = 0
    
    # 2. . 경우
    # -> 2개 일때 할당
    # -> 홀수 일때 끝
    # -> 0개 일때 무시 
    elif list_line[i] == '.':
        list_res[i] = '.'
        if cnt == 2:
            list_res[i-2: i] = 'BB' 
            cnt = 0
        elif cnt % 2 != 0:
            print(-1)
            quit()

# 계산2: 끝 할당
    # -> 2개 일때 할당
    # -> 홀수 일때 끝
    # -> 0개 일때 무시 
if cnt == 2:
    list_res[-1] = 'B'
    list_res[-2] = 'B'
elif cnt % 2 != 0:
    print(-1)
    quit()

# 출력
print(''.join(list_res))