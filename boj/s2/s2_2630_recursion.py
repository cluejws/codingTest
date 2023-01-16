def getResult(x, y, n):
    
    global white, blue
    value = graph[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            
            # 1,2,3,4 영역 재귀
            if value != graph[i][j]:
                getResult(x, y + n//2 , n//2)
                getResult(x, y, n//2)
                getResult(x + n//2, y, n//2)
                getResult(x + n//2, y + n//2, n//2)
                return
    
    if value == 0:
        white += 1
    elif value == 1:
        blue += 1        
        
           
# 입력
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

# 계산1: 초기화(자르기)
white = 0
blue = 0   
getResult(0,0, n)

# 출력
print(white, blue, sep='\n')