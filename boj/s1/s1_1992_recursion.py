def getResult(x,y,n):
    
    value = graph[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if value != graph[i][j]:
                
                res1 = getResult(x, y, n//2)
                #print(f'res1: {res1}')
                res2 = getResult(x, y + n//2, n//2)
                #print(f'res2: {res2}')
                res3 = getResult(x+ n//2, y, n//2)
                #print(f'res3: {res3}')
                res4 = getResult(x+ n//2, y+ n//2, n//2)
                #print(f'res4: {res4}')
                return '(' + res1 + res2 + res3 + res4 + ')'
    
    return str(value)


# 입력
import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip('\n')) for _ in range(n)]

# 계산1: 재귀를 통해 결과값 얻기
res = getResult(0,0, n)

# 출력
print(f'{res}')