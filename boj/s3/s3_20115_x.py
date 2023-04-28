def getResult(num):
    if num % 1 == 0:
        return int(num)
    
    return num

# 입력
import sys
input = sys.stdin.readline

n = int(input())
list_drink = list(map(int,input().split()))

# 계산1: 제일 작은것 + 제일 큰것
while len(list_drink) >= 2:
    
    # 1.
    min_drink = min(list_drink)
    max_drink = max(list_drink)
    list_drink.remove(min_drink)
    list_drink.remove(max_drink)

    # 2.
    list_drink.append(max_drink + (min_drink/2))

# 출력
print(getResult(list_drink[-1]))