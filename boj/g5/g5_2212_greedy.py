# 입력
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
list_pos = list(map(int,input().split()))

# 계산1: 좌표 정렬
list_pos.sort()

# 계산2: 차이 구하기
list_diff = [0 for _ in range(n-1)]
for i in range(n-1):
    list_diff[i] = list_pos[i+1] - list_pos[i]

# 계산3: 차이 정렬
list_diff.sort(reverse=True)

# 계산4: k-1개 만큼 빼기 -> 해당 구간 지워진 것
list_diff = list_diff[k-1:]

# 출력
print(sum(list_diff))