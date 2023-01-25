import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]

# 계산
cnt = 0
for i in range(n-1, -1, -1):
    
    coin = coins[i]
    if coin > k:
        continue
    
    
    cnt += k // coin
    k = k - (k // coin) * coin
    
# 출력
print(cnt)