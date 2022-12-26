num = int(input()) # 입력(총 개수)


int_list = [] # 입력(모든 수열)
for i in range(0,num):
    int_list.append(int(input()))

# ------------------------------------------------ #
stack_list = [0]
count = 0
print_list = []

# 수열 첫 데이터까지 과정
for i in range(1, int_list[0]+1):
    print_list.append("+")
    count += 1
    stack_list.append(count)
    
# 수열 다음 데이터까지 과정
for i in range(0, len(int_list)):
    
    #stack의 데이터와 같으면 pop
    if(int_list[i] == stack_list[-1]):
        print_list.append("-")
        stack_list.pop()
    
    #stack의 데이터보다 크면 push 
    elif(int_list[i] > stack_list[-1]):
        
        for j in range(count, int_list[i]):
            print_list.append("+")
            count += 1
            stack_list.append(count)
        
        print_list.append("-")
        stack_list.pop()

    #stack의 데이터보다 작으면 x
    else:
        print_list.append("NO")
        break

# 출력초과 방지
if(print_list[-1] == "NO"):
    print("NO")
else:
    for data in print_list:
        print(data)
    
