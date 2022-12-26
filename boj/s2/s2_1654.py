def check(mid):
    cnt = 0
    for a in arr:
       res = a // mid
       cnt += res
    
    global n
    if cnt >= n: return True
    else: return False 

# 입력
import sys
input = sys.stdin.readline

k , n = map(int,input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))
arr.sort()

# 계산
start = 0
end = max(arr)

while start + 1 < end:
    mid = (start+end) // 2
    
    if check(mid): start = mid
    else: end = mid
    
if check(end): print(end)
else: print(start)


