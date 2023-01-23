# 입력
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
line = input().strip()

# 계산1: i로 시작점 얻기
# IOIOII (0,2,4,5..)
arr = []
for i in range(m):
    if line[i] == 'O':
        continue
    else:
        arr.append(i) 

# 계산2:
# (현재,다음)차이가 2가 아니면 -> 누적 횟수 0
# (현재,다음)차이가 2면       -> 누적 횟수 += 1
# 누적횟수 비교  
res = 0
cnt = 0
for i in range(len(arr)-1):
    if arr[i+1] - arr[i] == 2:
        cnt += 1
    else:
        cnt = 0
    
    if cnt >= n:
        res += 1
        
# 출력        
print(res)