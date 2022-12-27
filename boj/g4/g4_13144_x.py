def isSame(slice_arr):
    
    data_dict = {}
    for data in slice_arr:
        if data not in data_dict:
            data_dict[data] = 1
        else:
            return True

    return False
        
# 입력
n = int(input())
arr = list(map(int, input().split()))

# 계산1: 모든 경우따라 중복 판단
# 경우의 수: i를 묶는 개수, j를 순서
cnt = len(arr)
for i in range(2,n+1):
    for j in range(n-i+1):
        slice_arr = arr[j:j+i] 
        if not isSame(slice_arr):
            cnt += 1

# 출력
print(cnt)