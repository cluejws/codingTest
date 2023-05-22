# 입력
n, k = map(int,input().split())
weight = []
value = []

for _ in range(n):
    w, v = map(int,input().split())
    weight.append(w)
    value.append(v)

# i: 1번째 부터 n번째까지 배낭 고려
# j: 무게
# dp[i][k]: i까지 고려했을때의 k무게 만큼 담고 후의 최대가치들
dp = [[0 for _ in range(k+1)] for _ in range(n)]

# 계산1: Tabulation위한 dp 초기화
for j in range(k+1):
    if j >= weight[0]:
        dp[0][j] = value[0]

# 계산2: dp 구하기
for i in range(1, n):
    for j in range(k+1):

        if j >= weight[i]:
            dp[i][j] = max(dp[i-1][j - weight[i]] + value[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

# 출력
print(dp[n-1][k])