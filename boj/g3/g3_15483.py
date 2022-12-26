# 입력
s1 = list(input())
s2 = list(input())

dp=[[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

# 계산1: dp초기화
dp[0][0] = 0
for i in range(1,len(s1)+1):
    dp[i][0] = dp[i-1][0] + 1

for j in range(1,len(s2)+1):
    dp[0][j] = dp[0][j-1] + 1

# 계산2: dp
for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

# 출력
print(dp[-1][-1])