# 입력
ip = input().split('-')

# 계산
res = 0
if len(ip) == 1: # -가 존재X ([1+1+1]
    arr = ip[0].split('+')
    for a in arr:
        res += int(a)

else:            # -가 존재O ([1+1+1, 20, 1])
    arr = ip[0].split('+')
    for a in arr:
        res += int(a)
    
    for i in range(1,len(ip)):

        if ip[i].isdigit():
            res -= int(ip[i])
        else:
            arr = ip[i].split('+')
            for a in arr:
                res -= int(a)
# 출력
print(res)