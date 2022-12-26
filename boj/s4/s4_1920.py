def find_num(num):
    
    start = 0
    end = len(n_list)-1
    
    if n_list[start] > num: return False
    if n_list[end] < num: return False
    
    while start <= end:
        
        mid = (start + end) // 2
        #print(f'({start},{end}) {mid}')
        if n_list[mid] > num:
            end = mid - 1
        elif n_list[mid] < num:
            start = mid + 1
        else:
            return True
        
    return False

# 입력    
n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int,input().split()))

# 계산 및 출력
for num in m_list:
    
    # 계산
    is_in = find_num(num)
    
    # 출력
    if is_in == True:
        print(1)
    else:
        print(0)