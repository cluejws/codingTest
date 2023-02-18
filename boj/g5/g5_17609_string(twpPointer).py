def getRemoveResult(line, start, end):
    
    while start <= end:
        if line[start] != line[end]:
            return False
        
        start += 1
        end -= 1
        
    return True

def getResult(line):
    
    # 계산: 투포인터
    start = 0
    end = len(line) - 1
    
    # 계산1: 삭제 개수
    cnt_pseudo = 0
    while start <= end:
        
        if line[start] != line[end]:
            
            isLeftRemove = getRemoveResult(line, start+1, end)
            isRightRemove = getRemoveResult(line, start , end-1)
            if isLeftRemove or isRightRemove:
                cnt_pseudo += 1
                break
                
            cnt_pseudo += 2
            break
            
        start += 1
        end -= 1
        
    if cnt_pseudo == 0:
        return 0
    elif cnt_pseudo == 1:
        return 1
    
    return 2

# 입력
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    line = input().rstrip()
    print(getResult(line))