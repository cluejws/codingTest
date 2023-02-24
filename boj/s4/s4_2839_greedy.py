# 입력
import sys
input = sys.stdin.readline

n = int(input())

# 계산:
# (1)5로 나눠떨어질 때
# (2)최대5 최소3으로 나눌떄
# (3)3로 나눠떨어질 때
# (4)나누어 떨어지지 않을 때
if n % 5 == 0:                  
    
    # (1)5로 나눠떨어질 때
    print(n // 5)
else:
    
    cnt = 0
    while n > 0:
        n -= 3
        cnt += 1
        
        if n % 5 == 0:          
            
            # (2)최대5 최소3으로 나눌떄
            cnt += n // 5
            print(cnt)
            break
        
        elif n == 0:            
            
            # (3)3로 나눠떨어질 때
            print(cnt)
        elif n == 1 or n == 2:    
            
            # (4)나누어 떨어지지 않을 때
            print(-1)
            break
        