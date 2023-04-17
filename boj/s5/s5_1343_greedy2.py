# 입력
import sys
input = sys.stdin.readline

list_line = input().rstrip()

# 계산: greedy
n = len(list_line)
list_res = ['.' for _ in range(n)]

i = 0
while i < n:
    if list_line[i:i+4] == 'XXXX':
        list_res[i:i+4] = 'AAAA'
        i += 4
    elif list_line[i:i+2] == 'XX':
        list_res[i:i+2] = 'BB'
        i += 2
    elif list_line[i] == 'X':
        print(-1)
        quit()
    else:
        i += 1

# 출력
print(''.join(list_res))