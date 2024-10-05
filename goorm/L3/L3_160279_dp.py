# 입력
n = int(input())

# 기저조건
if n == 1:
	print(5)
	quit()

# 계산1: dp 초기화
# dp[i][j] = i번째, j모양
dp = [[0 for _ in range(5)] for _ in range(n)]
for i in range(5):
	dp[0][i] = 1

# 계산2: dp
for i in range(1, n):
	# ooo
	dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4]) % 100000007
	
	# xoo
	dp[i][1] = (dp[i-1][0] + dp[i-1][3] + dp[i-1][4]) % 100000007
	
	# xox
	dp[i][2] = (dp[i-1][0] + dp[i-1][4]) % 100000007
	
	# oox
	dp[i][3] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][4]) % 100000007
	
	# oxo
	dp[i][4] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3]) % 100000007

# 출력
print(sum(dp[n-1]) % 100000007)