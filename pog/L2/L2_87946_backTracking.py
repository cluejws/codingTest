def makePermutation(n):
    def backTracking(cnt):
        # 기저조건
        if cnt == n:
            permus.append(permu[:])
            return
        
        for i in range(n):
            if visited[i] == False:
                visited[i] = True
                permu.append(i)
                backTracking(cnt + 1)
                permu.pop()
                visited[i] = False
    
    permus = []
    permu = []
    visited = [False for _ in range(n)]
    backTracking(0)
    
    return permus

def solution(k, dungeons):
    # 계산1: 순열
    n = len(dungeons)
    permus = makePermutation(n)
    
    # 계산2: 순열 순회
    max_cnt = 0
    for permu in permus:
        
        # 2-1: 최대 이동
        tired = k
        cnt = 0
        for idx in permu:
            # 0. 던전 정보
            d_min, d_tired = dungeons[idx]
            
            # 1: 최소 필요 피로도
            if tired < d_min:
                break
                
            # 2: 다음 반영
            tired -= d_tired
            cnt += 1
    
        # 2-2: 최대 이동 할당
        max_cnt = max(max_cnt, cnt)
    
    return max_cnt