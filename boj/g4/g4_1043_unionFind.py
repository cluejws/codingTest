def union(a,b):
    
    parent_a = find(a)
    parent_b = find(b)
    
    if parent_a != parent_b:
        parent[parent_b] = parent_a
    

def find(x):
    
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

# 입력
import sys
input = sys.stdin.readline

# n: 사람 수, m: 파티 수(입력)
n, m = map(int,input().split())
parent = [i for i in range(n+1)]

# 진실 아는 사람 수, 사람 번호들(입력)
# 경우가 달라짐 (없는 경우 / 있는 경우)
true_list = list(map(int,input().split()))

# 없는 경우
if len(true_list) == 1:
    
    # 계산1: 파티 오는 사람 수, 사람 번호들(입력)
    cnt = 0
    for _ in range(m):
        
        party = list(map(int,input().split()))
        cnt += 1
        
    # 출력
    print(cnt)
    
# 있는 경우
else:
    
    # 계산0: 진실 사람 번호들 slice
    true_list = true_list[1:]
     
    # 계산1: 파티 오는 사람 수, 사람 번호들(입력)
    # 경우가 달라짐 (파티 1명 / 파티 2명 이상)
    party_list = []
    for _ in range(m):
        
        
        party = list(map(int,input().split()))
        
        # 파티 1명
        if len(party) == 2:
            
            if party[1] not in true_list:
                party_list.append(party[1:])
            else:
                pass
          
        # 파티 2명 이상  
        else:
            for i in range(1, len(party)-1):    
                a = find(party[i])
                b = find(party[i+1])

                if a not in true_list and b in true_list:
                    union(b,a)
                elif a in true_list and b not in true_list:
                    union(a,b) 
                elif a in true_list and b in true_list:
                    union(a,b)
                else:
                    party_list.append(party[1:])
                    union(a,b)

    # 계산2: party_list에 담아 해당 진실 파티 판단 
    cnt = 0 
    for party in party_list:
        
        is_break = False
        for person in party:
            y = find(person)
            if y in true_list:
                is_break = True
                break
        
        if not is_break:
            cnt += 1
    
    # 출력
    print(cnt)