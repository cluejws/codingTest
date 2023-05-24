def getResult(prime, p):

    # 1. 18Cprime = (18! / prime! * (18-prime)!)
    sum18 = 1
    for i in range(1, (18)+1):
        sum18 *= i
    
    sumPrime = 1
    for i in range(1, (prime)+1):
        sumPrime *= i
    
    sum18MPrime = 1
    for i in range(1, (18-prime)+1):
        sum18MPrime *= i
    
    sumRes = sum18 / (sumPrime * sum18MPrime)

    # 2. 
    multiProbability = 1
    for i in range(1, (prime)+1):
        multiProbability *= p

    miltiMProbability = 1
    for i in range(1, (18-prime)+1):
        miltiMProbability *= (1-p)

    return sumRes * multiProbability * miltiMProbability

# 입력
import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

# 계산1: 확률 구하기
ap = a / 100
bp = b / 100

# 계산2: A가 소수일 확률 / B가 소수일 확률
sumA = 0
sumB = 0
list_prime = [2,3,5,7,11,13,17]
for i in list_prime:

    # 1. 확률 변수
    resA = getResult(i, ap)
    sumA += resA
    
    # 2. 확률 변수
    resB = getResult(i, bp)
    sumB += resB

# 계산3 및 출력: 1 - (A가 소수 아닐 확률) * (B가 소수 아닐 확률)
print(1 - (1 - sumA) * (1 - sumB))