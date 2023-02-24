# 입력
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
if m == 0:
    arr = []
else:
    arr = list(map(int,input().split()))
    
# 계산1: +,- 만 이동
min_cnt = abs(100 - n)
        
# 계산2: 완전탐색
# 엄밀히 말하면 n * 2 - 100 까지만 체크
for num in range(1000001):
    
    str_num = str(num)
    for i in range(len(str_num)):
        
        sn = str_num[i]
        if int(sn) in arr:
            break
        else:
            
            if i == len(str_num) - 1:
                cnt = len(str_num) + abs(n - num)
                min_cnt = min(cnt, min_cnt)
                
# 출력
print(min_cnt)        