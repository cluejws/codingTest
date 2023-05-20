def check(offset, graph, n):
    
    for i in range(n):
        for j in range(n):
            if graph[offset+i][offset+j] != 1:
                return False
    return True

def getRotateKey(key):
    
    m = len(key)
    rotateKey = [item[:] for item in key]
    for i in range(m):
        for j in range(m):
            rotateKey[j][m-1-i] = key[i][j]

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
    for _ in range(4):
        
        # 2.1: 회전
        key = getRotateKey(key)

        # 2.2: 판단
        for i in range(offset + n):
            for j in range(offset + n):
                
                # 1. 그래프 변형
                for x in range(m):
                    for y in range(m):
                        graph[i+x][j+y] += key[x][y]
                
                # 2. 판단
                if check(offset, graph, n):
                    return True
                
                # 3. 그래프 되돌리기
                for x in range(m):
                    for y in range(m):
                        graph[i+x][j+y] -= key[x][y]
    
    return False