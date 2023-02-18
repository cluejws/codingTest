# 입력
import sys
input = sys.stdin.readline

n = int(input())
dict_b = {}
for _ in range(n):
    a,b = input().rstrip().split('.')
    
    if b not in dict_b:
        dict_b[b] = 1
    else:
        dict_b[b] += 1
     
# 출력
sorted_items = sorted(dict_b.items())
for si in sorted_items:
    print(si[0], dict_b[si[0]])