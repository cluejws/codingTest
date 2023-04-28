# 입력
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

# 계산1: 정렬
nums.sort()

# 계산2: "M의 최소값" = "양쪽의 최대값"
# 홀: 최대값 or 양쪽 판단
# 짝: 양쪽 판단
max_res = 0
if n % 2 == 0:

    # 1.
    left = 0
    right = n - 1
    while left < right:
        max_res = max(max_res, nums[left] + nums[right])
        left += 1
        right -= 1

else:

    # 1.
    max_res = nums[-1]

    # 2.
    left = 0
    right = n - 2
    while left < right:
        max_res = max(max_res, nums[left] + nums[right])
        left += 1
        right -= 1

# 출력
print(max_res)