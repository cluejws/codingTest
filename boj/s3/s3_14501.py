# 입력
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

# dp[i] : i일(날짜)당 최대값
dp = [0 for _ in range(n)]

for i in range(n):                     
    
    # 해당 i일(날짜)선택 한 다음부터 비교
    for j in range( i+ arr[i][0], n):   
        print(dp,i)
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]

print(dp[-1])
