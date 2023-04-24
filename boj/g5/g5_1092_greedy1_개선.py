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
# continue (= 선택한 crane이 남아있는 박스 중 가장 가벼운 박스를 옮김x)
min_res = 0
while len(list_box) > 0:

    for i in range(n):
        crane = list_crane[i]
        
        # 1.
        if list_box and crane < list_box[-1]:
            continue
        
        # 2.
        for j in range(len(list_box)):
            box = list_box[j]
            if crane >= box:
                list_box.pop(j)
                break
    
    min_res += 1

# 출력
print(min_res)