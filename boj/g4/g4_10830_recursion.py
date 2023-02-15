def multiResult(graph_a, graph_b):
    
    res = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            
            sum_res = 0
            for k in range(n):
                sum_res += graph_a[x][k] * graph_b[k][y]

            res[x][y] = sum_res % 1000
            
    return res
            
def getResult(cnt):
    
    if cnt == 1:
        return graph
    else:
        res = getResult(cnt//2)        
        if cnt % 2 == 0:
            return multiResult(res, res)
        else:
            return multiResult(multiResult(res, res) , getResult(1))

# 입력
import sys
input = sys.stdin.readline

n, b = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# 계산: 재귀
res = getResult(b)

# 출력
for i in range(n):
    for j in range(n):
        print(res[i][j] % 1000, end=' ')
    
    print()