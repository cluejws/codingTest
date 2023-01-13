def printRes(i,j, arr):
    for k in range(len(arr)):
        if i == k or j == k:
            continue
        else:
            print(arr[k])

# 입력
arr = []
for _ in range(9):
    arr.append(int(input()))
    
# 계산1: 정렬
arr.sort()

# 계산2: twopointer
sum_res = sum(arr)
sum_res -= 100

j = len(arr) - 1
for i in range(len(arr)):
    
    # 계산2-1: 처음 판단
    if i < j and arr[i] + arr[j] == sum_res:
            
        printRes(i,j, arr)        
        quit()
    
    # 계산2-2: pointer 이동하면서 판단
    while i < j - 1 and arr[i] + arr[j] >= sum_res:
        j -= 1
        if i < j and arr[i] + arr[j] == sum_res:
            printRes(i,j, arr)
            quit()