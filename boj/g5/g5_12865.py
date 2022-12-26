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
dp = [[-1 for _ in range(k+1)] for _ in range(n)]
dp[0][0] = 0
if weight[0] <= k:
    dp[0][weight[0]] = value[0]

# 계산2: DP 구하기
for i in range(1,n):
    for j in range(k+1):

        if j >= weight[i] and dp[i-1][j - weight[i]] != -1:
            dp[i][j] = max(dp[i-1][j - weight[i]] + value[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

# 최대값 출력
max_num = 0
for i in range(len(dp)):
    max_dp = max(dp[i])
    if max_dp > max_num:
        max_num = max_dp
print(max_num)