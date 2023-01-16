# 입력
n, k = map(int,input().split())
weight = []
value = []

for _ in range(n):
    w, v = map(int,input().split())
    weight.append(w)
    value.append(v)

# 계산1: Tabulation위한 DP 초기화
# i: 0번째 부터 i번째까지 배낭 고려
# j: 무게
# dp[i][k]: i까지 고려했을때의 k무게 만큼 담고 후의 최대가치들
dp = [[0 for _ in range(k+1)] for _ in range(n)]

# 계산2: DP 구하기
for i in range(n):
    for j in range(k+1):

        if j >= weight[i]:
            dp[i][j] = max(dp[i-1][j - weight[i]] + value[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

# 출력
print(dp[n-1][k])