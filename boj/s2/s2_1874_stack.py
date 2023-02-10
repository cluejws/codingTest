# 입력
import sys
input = sys.stdin.readline

n = int(input())

# 계산
stack_list = []
print_list = []
cnt = 0

# 계산1: fault_flag로 판단
# 계산2: 첫번째 입력 ~ n번째 입력(cnt로 판단)
    # cnt >= k 면(k 도달할 때까지 pop)
    # cnt <  k 면(push해서 cnt+1 부터 k까지 만들고 pop)
fault_flag = False
for _ in range(n):
    
    k = int(input())

    # 계산1: fault_flag로 판단
    if fault_flag == True:
        continue

    # 계산2: cnt >= k
    if cnt >= k:
        
        # 계산2-1: k 도달 할떄까지 pop
        while True:
            
            if len(stack_list) != 0:
            
                data = stack_list.pop()
                print_list.append('-')
                if data == k:
                    break
            else:
                fault_flag = True
                break
            
    # 계산2: cnt < k 
    else:
        
        # 계산2-1: push해서 cnt+1 부터 k까지 만들고 pop
        for i in range(cnt + 1, k+1):
            cnt += 1
            stack_list.append(i)
            print_list.append('+')
        
        stack_list.pop()
        print_list.append('-')
           
# 출력
if fault_flag:
    print('NO')
else:
    for p in print_list:
        print(p)