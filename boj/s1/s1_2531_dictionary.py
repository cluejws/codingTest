# 입력
n,d,k,c = map(int,input().split())
arr = [int(input()) for _ in range(n)]

# 계산0: arr k만큼 추가
arr += arr[:k]

# 계산: sliding window
left = 0
right = 0
dict_num = {}
max_cnt = 0

# 계산1: k개만큼 먹기(right 1 추가된 상태)
while right < k:
    if arr[right] not in dict_num:
        dict_num[arr[right]] = 1
    else:
        dict_num[arr[right]] += 1
    
    right += 1

# 계산2: 쿠폰 포함
if c not in dict_num:
    dict_num[c] = 1
else:
    dict_num[c] += 1

# 계산3: sliding window
while left < n:
    
    # 계산3-1: 초밥 개수 세기
    max_cnt = max(max_cnt, len(dict_num))
    
    # 계산3-2: sliding window 이동
    dict_num[arr[left]] -= 1
    
    if dict_num[arr[left]] == 0:
        del dict_num[arr[left]]
    
    # 계산3-3: sliding window 초기화
    if arr[right] not in dict_num:
        dict_num[arr[right]] = 1
    else:
        dict_num[arr[right]] += 1
    
    left += 1
    right += 1
 
print(max_cnt)