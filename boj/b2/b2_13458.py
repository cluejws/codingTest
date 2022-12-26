n = int(input())                      # 시험장수

student = list(map(int,input().split()))  # 응시자수
main_p, sub_p = map(int,input().split())

cnt = 0
for st in student:
    
    # 계산0: 한 시험장의 응시자수
    res = st
    
    # 계산1: 총감독관
    res -= main_p
    cnt += 1
    
    if res <= 0:
        continue
    
    # 계산2: 부감독관
    temp_mok = res // sub_p
    temp_nam = res % sub_p
    
    if temp_nam != 0:
        temp_mok += 1
        cnt += temp_mok
    else:
        cnt += temp_mok
     
print(cnt)
    
