# 입력
n = int(input())
arr = list(map(int,input().split()))

# dp[i] = i 번째 까지 판단했을때 가장 큰 부분 수열의 합
dp = arr[:]

# 계산:
# i 번째 판단할때 
# 0 ~ i-1 -> dp[0 ~ i-1]의 최대
for i in range(1, n):

    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+ arr[i])

# 출력
print(max(dp))