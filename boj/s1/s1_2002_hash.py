# 입력
import sys
input = sys.stdin.readline

n = int(input())

dict_start = {} 
for i in range(n): 
    num = input().rstrip()
    dict_start[num] = i

list_end = []
for _ in range(n):
    num = input().rstrip()
    list_end.append(num)

# 계산: end 위치 이후 순서 판단
# {a: 0, b: 1, c: 2, d: 3} / [d, c, b, a] -> [3, 2, 1, 0] 
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if dict_start[list_end[i]] > dict_start[list_end[j]]:
            cnt += 1
            break

# 출력
print(cnt)