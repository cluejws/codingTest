import sys
input = sys.stdin.readline

# 입력
N = int(input())
M = int(input())

if M != 0:
    broken_button = [int(x) for x in input().split()]
else:
    broken_button = []

result = abs(100 - N)

# 완전탐색
for num in range(1000001):
    # num으로 0~100001까지 하나씩 비교
    num_arr = [int(x) for x in list(str(num))]

    
    for i in range(len(num_arr)):
        # 고장 남O
        if num_arr[i] in broken_button:
            break
        # 고장 남x
        else:
            if i == len(num_arr) - 1:
                count = len(num_arr) + abs(N - num)
                result = min(result, count)
print(result)