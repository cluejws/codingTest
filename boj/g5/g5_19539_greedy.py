# 입력
import sys
input = sys.stdin.readline

n = int(input())
list_tree = list(map(int,input().split()))

# 계산
# 1. 모든 나무가 자라는데 걸리는 횟수 = 전체 합 / 3
# 2. 2쓰는 횟수 >= 모든 나무가 자라는데 걸리는 횟수
if sum(list_tree) % 3 == 0:
    
    cnt = 0
    for tree in list_tree:
        cnt += tree // 2

    if (cnt) >= (sum(list_tree) // 3):
        print('YES')
    else:
        print('NO')

else:
    print('NO')