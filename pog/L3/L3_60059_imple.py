def check(offset, graph, n):
    
    for i in range(n):
        for j in range(n):
            if graph[offset+i][offset+j] != 1:
                return False
    return True

def getRotateKey(d, key):
    
    n = len(key)
    m = len(key[0])
    rotateKey = [item[:] for item in key]
    
    # 0도, 90도, 180도, 270도
    if d == 0:
        for i in range(n):
            for j in range(m):
                rotateKey[i][j] = key[i][j]

        return rotateKey
    
    elif d == 1:
        for i in range(n):
            for j in range(m):
                rotateKey[j][n-1-i] = key[i][j]

        return rotateKey
    
    elif d == 2:
        for i in range(n):
            for j in range(m):
                rotateKey[n-1-i][m-1-j] = key[i][j]

        return rotateKey
    
    elif d == 3:
        for i in range(n):
            for j in range(m):
                rotateKey[m-1-j][i] = key[i][j]

        return rotateKey

def solution(key, lock):
    
    n = len(lock)
    m = len(key)
    offset= (m - 1)
    length = n + 2 * offset

    # 계산1: 그래프 생성
    graph = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(offset, offset + n):
        for j in range(offset, offset + n):
            graph[i][j] = lock[i - offset][j - offset]
            
    # 계산2: 판단
    for i in range(offset + n):
        for j in range(offset + n):
            for d in range(4):
                
                rotateKey = getRotateKey(d, key)
                
                # 1. 그래프 변형
                for x in range(m):
                    for y in range(m):
                        graph[i+x][j+y] += rotateKey[x][y]
                
                # 2. 판단
                if check(offset, graph, n):
                    return True
                
                # 3. 그래프 되돌리기
                for x in range(m):
                    for y in range(m):
                        graph[i+x][j+y] -= rotateKey[x][y]
    
    return False