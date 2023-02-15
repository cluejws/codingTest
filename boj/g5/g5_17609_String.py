def check(line, left, right):
    
    while left < right:
        if line[left] == line[right]:
            left += 1
            right -= 1
        else:
            l_remove = check2(line, left+1, right)
            r_remove = check2(line, left, right-1)
            
            if l_remove or r_remove:
                return 1
            else:
                return 2
    
    return 0

def check2(line, left, right):
    
    while left < right:
        if line[left] == line[right]:
            left += 1
            right -= 1
        else:
            return False
        
    return True

# 입력
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    line = input().strip()
    
    left = 0
    right = len(line) - 1
    
    print(check(line, left, right))