def getResult(cnt, sum_res):
    if cnt == n-1:
        if sum_res == arr[n-1]:
            global res
            res += 1
        return
    
    if 0 <= sum_res + arr[cnt] <= 20:
        getResult(cnt + 1, sum_res + arr[cnt])
    
    if 0 <= sum_res - arr[cnt] <= 20:
        getResult(cnt + 1, sum_res - arr[cnt])

# 입력
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

# 계산: dfs
res = 0
getResult(1, arr[0])

# 출력
print(res)