# 입력
t = int(input().rstrip())

for _ in range(t):
    
    # 입력
    str_ip = input().rstrip()
    
    # 계산
    front_res = []
    back_res = []

    for s in str_ip:
        
        if s == '<':
            if len(front_res) == 0:
                continue
            else:
                pop_data = front_res.pop()
                back_res.append(pop_data)

        elif s == '>':
            if len(back_res) == 0:

                continue
            else:
                pop_data = back_res.pop()
                front_res.append(pop_data)
        
        elif s == '-':
            if len(front_res) == 0:
                continue
            else:
                pop_data = front_res.pop()        
        else:
            front_res.append(s)
    
    # 출력    
    front_str = ''.join(front_res)
    
    back_res.reverse() 
    back_str = ''.join(back_res)
    
    print(front_str + back_str)
