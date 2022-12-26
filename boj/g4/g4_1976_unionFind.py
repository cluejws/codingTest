def union(a,b):
    
    root_a = find(a)
    root_b = find(b)
    
    if root_a != root_b:
        parent[root_b] = parent[root_a]
        return True
    else:
        return False
    
def find(x):
    
    if x == parent[x]:
        return x
    
    y = find(parent[x])
    parent[x] = y
    return y

def getResult(start, end):
    
    root_start = find(start)
    root_end = find(end)
    
    if root_start == root_end:
        return True
    else:
        return False    

# 입력
n = int(input())
m = int(input())

# 계산1: union 그룹 만들기
parent = [i for i in range(n)]
for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(len(arr)):
        
        res = arr[j]
        if res == 1 and not getResult(i,j):
            union(i,j)

# 계산2: 
# 시작, 끝 통해 연결 판단 
# 단 중간에 안되면 끝
path = list(map(int,input().split()))
for i in range(m-1):
    if not getResult(path[i]-1 , path[i+1]-1):
        print('NO')
        quit()

print('YES')