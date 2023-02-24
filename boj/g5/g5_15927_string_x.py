def isNotPalindrome(left, right):
    
    while left <= right:
        if line[left] == line[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

def getResult(left, right):

    # 기저조건1: 포인터 위치     
    if left > right:
        return
    
    # 기저조건2: 할당
    global max_res
    if isNotPalindrome(left, right):
        max_res = max(max_res, right - left + 1)
        return 
    
    getResult(left + 1, right)
    getResult(left, right - 1)

# 입력
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

line = input().rstrip()

# 계산
max_res = 0
getResult(0, len(line) - 1)

# 출력
if max_res == 0:
    print(-1)
else:
    print(max_res)