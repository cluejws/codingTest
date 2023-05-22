# 입력
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
list_alp = [(input().rstrip()) for _ in range(n)]

# 계산1: 문자열 길이 총합
len_cnt = 0
for alp in list_alp:
    len_cnt += len(alp)

# 계산2: 추가 판단X
mod = (m - len_cnt) % (n - 1)
temp = '_' * ((m - len_cnt) // (n - 1))
if mod == 0:
    print(temp.join(list_alp))
    quit()

# 계산3: 추가 판단O(소문자 앞쪽부터 / 뒤쪽부터)
# 3-1. 소문자 앞쪽부터 얻기
plus_temp = []
for i in range(1, n):
    if ord('a') <= ord(list_alp[i][0]) <= ord('z'):
        plus_temp.append(i)

# 3.2. 뒤쪽부터 얻기(추가)
if mod > len(plus_temp):
    plus_len = mod - len(plus_temp)
    plus_cnt = 0
    for i in range(n-1, -1, -1):
        if plus_cnt == plus_len:
            break
        if i not in plus_temp:
            plus_temp.append(i)
            plus_cnt += 1

# 계산4: 반영
res = list_alp[0]
cnt = 0
for i in range(1, n):
    alp = list_alp[i]
    if cnt < mod and i in plus_temp:
        res += (temp + '_' + alp)
        cnt += 1
    else:
        res += (temp + alp)
print(res)