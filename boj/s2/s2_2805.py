def check(value):
    
    # 남은 높이 합
    sum = 0
    for a in arr:
        if a > value:
            sum += (a-value)
    
    global m
    if sum >= m:
        return True
    else:
        return False

# 입력 
n,m = map(int,input().split())
arr = list(map(int,input().split()))

# 계산
h = 0

start = 0
end = max(arr)

while start <= end:
    
    mid = (start + end) // 2
    if check(mid) == True:
        h = mid
        start = mid + 1
    else:
        end = mid - 1 

print(h)