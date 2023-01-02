n, k = map(int,input().split())
dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

# 1개의 수로 j 만들기
for j in range(n+1):
    dp[1][j] = (1) % 1000000000

if k <= 1:
    print(dp[k][n])
    quit()

# 2개의 수로 j 만들기
for j in range(n+1):
    dp[2][j] = (j+1) % 1000000000
    
if k <= 2:
    print(dp[k][n])
    quit()
    
# i(k)개의 수로 j(n)만들기
for i in range(3, k+1):
    for j in range(n+1):
        
        sum_res = 0
        for j_index in range(j+1):
            sum_res += dp[i-1][j_index]
        
        dp[i][j] = sum_res % 1000000000
        
print(dp[k][n])