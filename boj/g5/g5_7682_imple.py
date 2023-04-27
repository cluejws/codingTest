def getCnt(list_line):
    xcnt = 0
    ocnt = 0
    # 좌우
    for i in range(3):
        if list_line[i][0] == list_line[i][1] and list_line[i][1] == list_line[i][2]:
            if list_line[i][0] == 'X':
                xcnt += 1
            elif list_line[i][0] == 'O':
                ocnt += 1
    
    # 상하
    for j in range(3):
        if list_line[0][j] == list_line[1][j] and list_line[1][j] == list_line[2][j]:
            if list_line[0][j] == 'X':
                xcnt += 1
            elif list_line[0][j] == 'O':
                ocnt += 1

    # 대각선
    if list_line[0][0] == list_line[1][1] and list_line[1][1] == list_line[2][2]:
        if list_line[0][0] == 'X':
            xcnt += 1
        elif list_line[0][0] == 'O':
            ocnt += 1

    if list_line[2][0] == list_line[1][1] and list_line[1][1] == list_line[0][2]:
        if list_line[2][0] == 'X':
            xcnt += 1
        elif list_line[2][0] == 'O':
            ocnt += 1

    return xcnt, ocnt

def check(list_line, diff):

    xcnt, ocnt = getCnt(list_line)

    # 1개 차이 -> X연속2개, X연속1개, 둘다0개+꽉참
    if diff == 1:
        if xcnt == 2 and ocnt == 0:
            return True
        if xcnt == 1 and ocnt == 0:
            return True
        if xcnt == 0 and ocnt == 0 and isAll(list_line):
            return True

    # 0개 차이 -> O연속1개
    elif diff == 0:
        if xcnt == 0 and ocnt == 1:
            return True
        
    return False
        
def isAll(list_line):

    for i in range(3):
        if '.' in list_line[i]:
            return False
        
    return True

# 입력
import sys
input = sys.stdin.readline

while True:

    # 종료 조건
    line = input().rstrip()
    if line == 'end':
        break

    # 계산1: 배열화
    list_line = [['' for _ in range(3)] for _ in range(3)]
    cnt = 0
    for i in range(3):
        for j in range(3):
            list_line[i][j] = line[cnt]
            cnt += 1

    # 계산2: X, O 개수 세기
    xcnt = 0
    ocnt = 0
    for i in range(3):
        for j in range(3):
            if list_line[i][j] == 'X':
                xcnt += 1
            elif list_line[i][j] == 'O':
                ocnt += 1
    diff = xcnt - ocnt

    # 계산3: X > O(1개 차), X = O(0개 차) 경우 나누기
    if diff == 1:
        print('valid' if check(list_line, diff) else 'invalid')
    elif diff == 0:
        print('valid' if check(list_line, diff) else 'invalid')
    else:
        print('invalid')