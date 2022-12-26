def union(a,b,cnt):
    root_a = find(a)
    root_b = find(b)
    
    if root_a != root_b:
        parent[root_b] = root_a
        temp_cnt = cnt
        temp_cnt += network[root_b]
        network[root_a] = temp_cnt
        network[root_b] = temp_cnt
        return network[root_a]
       
def find(x):
    
    if x == parent[x]:
        return x

    else:
        y = find(parent[x])
        parent[x] = y
        return y

t = int(input())
for _ in range(t):
    
    # 초기 조건
    f = int(input()) 
    network = []
    
    parent = []
        
    people = []
    people_idx = 0 
    
    # 입력 a,b 추가    
    a,b = input().split()
    people.append((a,people_idx))
    parent.append(people_idx)
    network.append(1)
    people_idx += 1

    people.append((b,people_idx))
    parent.append(people_idx)
    network.append(1)
    people_idx += 1
    
    # 출력
    root_a = find(0)
    print(union(people[0][1], people[1][1], network[root_a]))


    for _ in range(1,f):
        
        c,d = input().split()
        
        # 입력 c 추가
        is_c_break = False
        is_c_idx = people_idx
        for i in range(len(people)):
            name, idx = people[i]
            if c == name:
                is_c_idx = idx
                is_c_break = True
                break
        
        if is_c_break == False:
            people.append((c,people_idx))
            parent.append(people_idx)
            network.append(1)
            people_idx += 1
        else:
            pass
            
        # 입력 d 추가
        is_d_break = False
        is_d_idx = people_idx
        for i in range(len(people)):
            name, idx = people[i]
            if d == name:
                is_d_idx = idx
                is_d_break = True
                break
            
        if is_d_break == False:
            people.append((d,people_idx))
            parent.append(people_idx)
            network.append(1)
            people_idx += 1
        
        # 계산
        if is_c_break == False and is_d_break == False:
            #새로운 관계
            root_c = find(is_c_idx)
            print(union(is_c_idx, is_d_idx, network[root_c]))
        else:
            # 기존관계
            if is_c_break == True:
                root_c = find(is_c_idx)
                print(union(is_c_idx, is_d_idx, network[root_c]))

            elif is_d_break == True:
                root_d = find(is_d_idx)
                print(union(is_d_idx, is_c_idx, network[root_d]))