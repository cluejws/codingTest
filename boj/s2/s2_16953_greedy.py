# 입력
import sys
input = sys.stdin.readline

a, b = map(int,input().split())

# 계산: greedy
cnt = 1
while a <= b:

    if a == b:
        print(cnt)
        quit()

    elif b % 10 == 1:
        b = b // 10
        cnt += 1
    
    elif b % 2 == 0:
        b = b // 2
        cnt += 1

    else:
        print(-1)
        quit()

# 출력
print(-1)