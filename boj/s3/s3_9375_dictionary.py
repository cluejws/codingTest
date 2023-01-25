import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    n = int(input())
    
    # 계산1: dictonary 구성    
    dict_clothes = {}
    for _ in range(n):
        name, kind = input().split()
        if kind not in dict_clothes:
            dict_clothes[kind] = [name]
        else:
            dict_clothes[kind].append(name)

    # 계산2: 조합 계산(아무것도 입지 않은 경우 각각 포함)
    cnt = 1
    for key in dict_clothes:
        cnt = cnt * (len(dict_clothes[key]) + 1)
    
    # 계산3: 조합 - 1    
    cnt -= 1
    
    # 출력
    print(cnt)