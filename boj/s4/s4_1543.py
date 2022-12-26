# 입력
str_in = input().rstrip()
for_str_in = input().rstrip()

# 계산
length = len(for_str_in)

cnt = 0 
res = 0
while cnt != len(str_in):
    
    # 계산1: str_in문자와 for_str_in만큼 비교
    # str_in 끝 문자에서 초과되면 안됨
    if length+cnt > len(str_in):
        break
    
    is_break = False    
    for j in range(cnt, length+cnt):
        if str_in[j] == for_str_in[j-cnt]:
            continue
        else:
            is_break = True
            break 
         
    # 계산2: 
    # 일치 -> 길이추가, 다음idx부터
    # 일치x -> 길이추가x, +1부터
    if is_break == False:
        res += 1
        cnt += length
    else:
        cnt += 1

# 출력
print(res)
        