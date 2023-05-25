def change(temp_now, temp_target):

    # 계산1: 이전 위치 비교 -> 바꾸기
    cnt = 0
    for i in range(1, n):
        if temp_now[i-1] != temp_target[i-1]:
            
            # 1.
            cnt += 1

            # 2.
            temp_now[i-1] = abs(temp_now[i-1] - 1)
            temp_now[i] = abs(temp_now[i] - 1)
            if i + 1 < n:
                temp_now[i+1] = abs(temp_now[i+1] - 1)

    # 계산2: 판단
    if check(temp_now, temp_target):
        return cnt
    else:
        return math.inf

def check(temp_now, temp_target):
    for i in range(n):
        if temp_now[i] != temp_target[i]:
            return False
    
    return True

# 입력
import sys, math
input = sys.stdin.readline

n = int(input())
list_now = list(map(int, list(input().rstrip())))
list_target = list(map(int, list(input().rstrip())))

# 계산1: 처음 바꾸기X
noCnt = change(list_now[:], list_target[:])

# 계산2: 처음 바꾸기O
list_now[0] = abs(list_now[0] - 1)
list_now[1] = abs(list_now[1] - 1)
yesCnt = change(list_now[:], list_target[:])

# 출력
if noCnt == math.inf and yesCnt == math.inf:
    print(-1)
else:
    print(min(noCnt, yesCnt+1))