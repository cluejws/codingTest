# 입력
import sys
input = sys.stdin.readline

n = int(input())
list_crane = list(map(int,input().split()))
m = int(input())
list_box = list(map(int,input().split()))

# 계산0: 크레인, 박스 정렬
list_crane.sort(reverse=True)
list_box.sort(reverse=True)

# 계산1: 박스 옮길 수 있는 지 판단
if list_crane[0] < list_box[0]:
    print(-1)
    quit()

# 계산2: 그리디
# crane 순회 -> 최대 box 삭제
min_res = 0
while len(list_box) > 0:

    for i in range(n):
        crane = list_crane[i]
        for j in range(len(list_box)):
            box = list_box[j]
            if crane >= box:
                list_box.pop(j)
                break
    
    min_res += 1

# 출력
print(min_res)