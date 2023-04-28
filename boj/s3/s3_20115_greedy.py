def getResult(num):
    if num % 1 == 0:
        return int(num)
    
    return num

# 입력
import sys
input = sys.stdin.readline

n = int(input())
list_drink = list(map(int,input().split()))

# 계산0: 정렬
list_drink.sort(reverse=True)

# 계산1: 제일 큰것 + 나머지/2
sum_drink = list_drink[0]
for i in range(1, n):
    sum_drink += (list_drink[i] / 2)

# 출력
print(getResult(sum_drink))