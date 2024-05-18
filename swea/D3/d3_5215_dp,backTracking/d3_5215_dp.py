import sys
sys.stdin = open("sample_input.txt", "r")

# 입력
t = int(input())
for tc in range(t):

    # 입력
    n, l = map(int,input().split())
    foods = [list(map(int,input().split())) for _ in range(n)]

    # 계산1: Tabulation 위한 DP 초기화
    # i: 0번째 부터 n번째 까지 재료 고려
    # j: 칼로리
    # dp[i][k]: i까지 고려했을때의 k 칼로리 만큼 담고 후의 최대 점수
    dp = [[0 for _ in range(l + 1)] for _ in range(n)]

    # 계산2: DP 구하기
    for i in range(n):
        for j in range(l + 1):

            score, calorie = foods[i]
            if j >= calorie:
                dp[i][j] = max(dp[i - 1][j - calorie] + score, dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    # 출력
    print(f'#{tc+1} {dp[n - 1][l]}')