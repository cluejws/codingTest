def getResult(date, sum): # date:현재날짜, sum:현재합
    
    # print(f"date: {date} sum:{sum}")
    # 할당
    global res
    if sum > res:
        res = sum

    # 완전탐색(cnt: 다음 날짜를 선택 할 때마다 1을 더해줘야됨)
    cnt = 0
    for k in range(date, n):
        
        now_date = cnt + date + arr[k][0]
        now_value = sum + arr[k][1] 
        cnt += 1
        
        if now_date <= n:
            getResult(now_date, now_value)      


# 입력: 날짜[0], 값[1]
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

# 계산
res = 0
getResult(0,0) # 시작: 0일, 0값

# 출력
print(res)
