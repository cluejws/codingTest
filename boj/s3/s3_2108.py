# 입력
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
arr.sort()

# 출력
# 1. 산술평균
# 2. 중앙값
# 3. 최빈값
# 4. 범위 -> 최대값 - 최소값

p_1 = round(sum(arr) / n)
p_2 = arr[n//2]

if n != 1:
    dict_3 = {}
    for a in arr:
        if a in dict_3:
            dict_3[a] +=1
        else:
            dict_3[a] = 1
    sorted_dict_3 = sorted(dict_3.items(), key=lambda x: (-x[1], x[0]))
    if sorted_dict_3[0][1] == sorted_dict_3[1][1]:
        p_3 = sorted_dict_3[1][0]
    else:
        p_3 = sorted_dict_3[0][0]
else:
    p_3 = arr[0]
    
p_4 = arr[-1] - arr[0]

print(p_1,p_2,p_3,p_4, sep="\n")

