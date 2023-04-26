# 입력
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
nums = input().rstrip()

# 계산1: 빼기
stack = []
cnt = 0
for num in nums:

    while len(stack) > 0 and stack[-1] < num and cnt < k:
        cnt += 1
        stack.pop()
    
    stack.append(num)

# 계산2 및 출력: k 만큼 안뺄 경우
if cnt == k:
    print(''.join(stack))
else:
    for _ in range(k-cnt):
        stack.pop()
    print(''.join(stack))