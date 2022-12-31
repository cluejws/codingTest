def getCnt(arr, k, c):
    
    # 계산: 
    # k만큼 추가 후 반복문 돌면서 k 만큼 slice / 초밥 개수 판단
    max_cnt = 0 
    temp_arr = arr[:] + arr[:k]
    for i in range(n):
        
        # 계산1: slice
        slice_arr = temp_arr[i:i+k]
        
        # 계산2: 초밥 개수 판단
        set_arr = set(slice_arr)
        cnt = len(set_arr)
        if c not in set_arr:
            cnt += 1    
        
        # 계산3: 최대값 얻기
        max_cnt = max(max_cnt, cnt)
    
    return max_cnt
    
n,d,k,c = map(int,input().split())
arr = [int(input()) for _ in range(n)]
print(getCnt(arr,k,c))