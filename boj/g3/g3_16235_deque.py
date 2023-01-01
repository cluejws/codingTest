def check(x,y):
    if 1<=x<=n and 1<=y<=n:
        return True
    else:
        return False

def putTree(i,j):
    
    if check(i-1,j-1):
        trees[i-1][j-1].appendleft(1)
    if check(i-1, j):
        trees[i-1][j].appendleft(1)
    if check(i-1, j+1):
        trees[i-1][j+1].appendleft(1)
    if check(i,j-1):
        trees[i][j-1].appendleft(1)
    if check(i,j+1):
        trees[i][j+1].appendleft(1)
    if check(i+1,j-1):
        trees[i+1][j-1].appendleft(1)
    if check(i+1,j):
        trees[i+1][j].appendleft(1)
    if check(i+1,j+1):
        trees[i+1][j+1].appendleft(1)

# 입력
from collections import deque
n,m,k = map(int,input().split())

# 땅에 양분 초기화
graph = [[5 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
    graph[i][0] = -1
    graph[0][i] = -1

# 겨울에 양분 추가량 초기화
A = [[-1 for _ in range(n+1)]]
for _ in range(n):
    A.append([-1] + list(map(int,input().split())))
    
# 나무 초기화
# 입력으로 주어지는 나무위치 서로달라서 정렬 필요X
trees = [[deque() for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    x,y,z = map(int,input().split())
    trees[x][y].append(z)

# 계산:
# k 동안 봄,여름,가을,겨울 함수 진행
# 가을: 새로생기는 제일 어린나무이기에 앞에 넣어 정렬
for _ in range(k):
    
    # 계산1: 봄 + 여름
    dieTree = deque()
    for i in range(1, n+1):
        for j in range(1, n+1):
            
            init_len = len(trees[i][j])
            for k in range(init_len):
                
                age = trees[i][j][k]    
                if age <= graph[i][j]:
                    graph[i][j] -= age
                    trees[i][j][k] += 1
                else:
                    for _ in range(k, init_len):
                        pop_age = trees[i][j].pop()
                        graph[i][j] += (pop_age // 2)
                    break

    # 계산2: 가을 + 겨울
    for i in range(1, n+1):
        for j in range(1, n+1):
            
            init_len = len(trees[i][j])
            for k in range(init_len):
                age = trees[i][j][k]  
                if age % 5 == 0:
                    putTree(i,j)

            graph[i][j] += A[i][j]

# 출력
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        cnt += len(trees[i][j]) 
print(cnt)