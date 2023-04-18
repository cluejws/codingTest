# 입력
import sys
input = sys.stdin.readline

list_line = input().rstrip()

# 계산1: M, K 판단
max_res = ''
min_res = ''
cnt = 0
for line in list_line:

    if line == 'M':
        cnt += 1
    
    elif line == 'K':
        if cnt > 0:
            max_res += str(5 * (10 ** cnt)) 
            min_res += str(10 ** (cnt - 1)) + '5'
        else:
            max_res += '5'
            min_res += '5'

        cnt = 0

# 계산2: M으로 끝날 경우
if cnt > 0:
    max_res += '1' * cnt
    min_res += str(10 ** (cnt - 1))

# 출력: 최대 최소
print(max_res)
print(min_res)