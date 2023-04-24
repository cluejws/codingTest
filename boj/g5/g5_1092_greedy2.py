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
# crane 순회
# position[i]가 m을 초과 (= 선택한 crane이 남아있는 박스 중 가장 가벼운 박스를 옮김)
# box위치 -> position[i] (position[i]을 통해 이전 box위치 기록)
# box위치 방문 여부 -> visited[position[i]]  
min_res = 0
position = [0 for _ in range(n)]
visited = [False for _ in range(m)]
cnt = 0
while cnt < m:

    for i in range(n):
        crane = list_crane[i]
        while position[i] < m:
            if crane >= list_box[position[i]] and visited[position[i]] == False:
                visited[position[i]] = True
                position[i] += 1
                cnt += 1
                break
            else:
                position[i] += 1
    
    min_res += 1

# 출력
print(min_res)