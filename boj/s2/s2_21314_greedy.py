def getMax():

    # K 없을 때
    if len(list_pos) == 0:
        return '1' * len(list_line)

    else:
        # 1. K 위치로 판단
        max_res = str(5 * (10 ** list_pos[0]))
        for i in range(1, len(list_pos)):
            cnt = list_pos[i] - list_pos[i-1] - 1
            max_res += str(5 * (10 ** cnt))

        # 2. K가 끝이 아닐 경우
        if list_pos[-1] != n-1:
            max_res += '1' * ((n-1) - list_pos[-1])

        return max_res

def getMin():
    
    # K 없을 때
    if len(list_pos) == 0:
        return str(10 ** (n-1)) 

    else:
        # 1. K 위치로 판단
        min_res = ''
        if list_pos[0] == 0:
            min_res += '5'
        else:
            min_res = str(10 ** (list_pos[0] - 1)) + '5'
        

        for i in range(1, len(list_pos)):
            if list_pos[i] - list_pos[i-1] == 1:
                min_res += '5'
            else:
                cnt = list_pos[i] - list_pos[i-1] - 2
                min_res += str(10 ** cnt) + '5'

        # 2. K가 끝이 아닐 경우
        if list_pos[-1] != n-1:
            min_res += str(10 ** ((n-1) - list_pos[-1] - 1)) 
        
        return min_res

# 입력
import sys
input = sys.stdin.readline

list_line = input().rstrip()

# 계산1: K 위치 얻기
n = len(list_line)
list_pos = []
for i in range(n):
    line = list_line[i]
    if line == 'K':
        list_pos.append(i)

# 계산 및 출력: 최대 최소
print(getMax())
print(getMin())