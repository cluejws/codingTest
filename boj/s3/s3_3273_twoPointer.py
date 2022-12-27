# 입력
n = int(input())
arr = [0] + list(map(int,input().split()))
x = int(input())

# 계산0: 정렬
arr.sort()

# 계산1: twoPointer(cnt)
cnt = 0
j = n
for i in range(1, n+1):
    
    # 계산1-0: 최대길이 구하기
    while j != 1 and arr[i] + arr[j] > x:
        j -= 1
    
    # 계산1-2: 개수 구하기
    if j <= i:
        break
    else:
        if arr[i] + arr[j] == x:
            cnt += 1 

print(cnt)