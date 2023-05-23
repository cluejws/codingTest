# 입력
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
list_length = list(map(int,input().split()))

# 계산1: 오름차순 정렬
list_length.sort()

# 계산2: 10배수 인덱스 얻기
ten_list = []
for i in range(n):
    length = list_length[i]
    if length % 10 == 0:
        ten_list.append(i)

# 계산3: 10배수 인덱스 m번 자름
max_res = 0
cnt = 0
for i in ten_list:

    # 0. 기저조건
    if cnt == m:
        break

    # 1. 10 -> 자름X
    length = list_length[i]
    if length == 10:
        max_res += 1
        continue

    # 2. 10배수 -> 자름O
    # (m - cnt) >= 자를수 있는 횟수 -> 자를 수 있는 횟수
    # (m - cnt) <  자를수 있는 횟수 -> (m - cnt)
    sliceCnt = (length // 10) - 1
    if (m - cnt) >= sliceCnt:
        max_res += sliceCnt + 1
        cnt += sliceCnt
    else:
        if sliceCnt == 1:
            max_res += (m - cnt) + 1
        else:
            max_res += (m - cnt)
        cnt += (m - cnt)

# 계산4: (10보다 큰 것) 추가 자름
if cnt < m:

    for i in range(n):
    
        # 0. 기저조건
        if cnt == m:
            break

        # 1. 10배수(이미 자름) -> 자름X
        if i in ten_list:
            continue

        # 2. 10보다 작음 -> 자름X
        length = list_length[i]
        if length < 10:
            continue

        # 3. 10보다 큼 -> 자름O
        # (m - cnt) >= 자를수 있는 횟수 -> 자를 수 있는 횟수
        # (m - cnt) <  자를수 있는 횟수 -> (m - cnt)
        sliceCnt = (length // 10)
        if (m - cnt) >= sliceCnt:
            max_res += sliceCnt
            cnt += sliceCnt
        else:
            max_res += (m - cnt)
            cnt += (m - cnt)
    
# 출력
print(max_res)