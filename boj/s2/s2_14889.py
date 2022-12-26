def getResult():
    
    # 계산1: start 그룹 값
    start_value = 0
    for i in range(len(start_group)):
        for j in range(i+1, len(start_group)):
            start_value += (graph[start_group[i]][start_group[j]] + graph[start_group[j]][start_group[i]])
    
    # 계산2: link_group 구하기
    link_group = []
    for i in range(n):
        if i not in start_group:
            link_group.append(i)
    
    # 계산3: link 그룹 값
    link_value = 0
    for i in range(len(link_group)):
        for j in range(i+1, len(link_group)):
            link_value += (graph[link_group[i]][link_group[j]] + graph[link_group[j]][link_group[i]])

    # 계산4: 절대값 return
    return abs(start_value - link_value)

def dfs(cnt, start):
    
    # 기저조건
    if cnt == (n//2) :
        global min_res
        result = getResult()
        if min_res > result:
            min_res = result
        return

    # group 할당
    for i in range(start,n):
        start_group[cnt] = i
        dfs(cnt+1, i+1)
        start_group[cnt] = -1

# 입력
import math

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int,input().split()))

# 계산: 경우의 수 통해 최소값 구하기
start_group = [-1 for _ in range(n//2)]

min_res = math.inf
dfs(0,0)

# 출력
print(min_res)