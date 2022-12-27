# 입력
n = int(input())
arr = [0] + list(map(int,input().split()))

# 계산: TwoPointer
cnt = 0
j = 0
count_arr = [0 for _ in range(100000 + 1)]
for i in range(1, n + 1):
    
    # 계산1: 중복되지 않는 최대 구간 구하기
    while j + 1 <= n and count_arr[arr[j+1]] == 0:
        count_arr[arr[j + 1]] = 1
        j += 1
        
    # 계산2: 해당 구간에서 i를 포함하는 개수 구하기
    cnt += j - i + 1
    
    # 계산3: 
	# 다음 구간으로 넘어가기 전에
    # arr[i]에 해당하는 값은 count_arr에서 지움
    count_arr[arr[i]] -= 1

print(cnt)