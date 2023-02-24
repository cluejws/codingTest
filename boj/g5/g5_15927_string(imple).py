def isPalindrome(left, right):
    
    while left <= right:
        if line[left] != line[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

def isAllSame():
    
    for i in range(1, len(line)):
        if line[0] != line[i]:
            return False
    
    return True

# 입력
import sys
input = sys.stdin.readline

line = input().rstrip()

# 계산
# palindrome o 
#   -> 모두 같으면 -1
#   -> 하나라도 다르면 최대값
# palindrome x 
#   -> 최대값 
max_res = -1
if isPalindrome(0, len(line)-1):
    
    if isAllSame():
        max_res = -1
    else:
        max_res = len(line) - 1

else:
    max_res = len(line)

# 출력
print(max_res)