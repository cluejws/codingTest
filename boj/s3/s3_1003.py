import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    
    a = int(input())
    dp_0 = [0 for _ in range(a+1)]
    dp_1 = [0 for _ in range(a+1)]
    
    if a >= 1:

        dp_0[0] = 1
        dp_0[1] = 0

        dp_1[0] = 0
        dp_1[1] = 1
 
        for i in range(2,a+1):
            dp_0[i] = dp_0[i-1] + dp_0[i-2]
            dp_1[i] = dp_1[i-1] + dp_1[i-2]
    
        print(dp_0[a], dp_1[a])
    
    else:    
        dp_0[0] = 1
        
        dp_1[0] = 0
        
        print(dp_0[a], dp_1[a])
