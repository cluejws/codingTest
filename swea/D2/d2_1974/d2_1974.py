def a():
    for i in range(9):
        if len(arr[i]) != len(set(arr[i])):
            return False

    return True

def b():
    for j in range(9):

        temp = []
        for i in range(9):
            if arr[i][j] in temp:
                return False

            temp.append(arr[i][j])

    return True

def c():
    for i in range(0,7,3):
        for j in range(0,7,3):

            temp = []
            for x in range(3):
                for y in range(3):
                    if arr[i+x][j+y] in temp:
                        return False

                    temp.append(arr[i+x][j+y])

    return True

import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(t):

    # 1. 입력
    arr = [list(map(int,input().split())) for _ in range(9)]

    # 2. 계산(가로/세로/3칸)
    if a() and b() and c():
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')