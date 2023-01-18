# 입력
n = int(input())
arr = list(map(int,input().split()))

# 계산1: 정렬
arr.sort()

# 계산2: arr[1] ... 순서 부터 계산
time = arr[0]
pre_time = arr[0]
for i in range(1, len(arr)):
    
    pre_time += arr[i]
    time += pre_time

# 출력
print(time)