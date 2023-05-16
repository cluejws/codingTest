# 입력
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
list_pos = list(map(int, input().split()))

# 계산0: 정렬
list_pos.sort()

# 계산1: 위치 순회 -> 위치의 범위 판단
cnt = 1
start = list_pos[0] - 0.5
end = start + l 
for i in range(n):
    if start <= list_pos[i] <= end:
        continue

    cnt += 1
    start = list_pos[i] - 0.5
    end = start + l

# 출력
print(cnt)