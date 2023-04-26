def solution(name):
    
    # 계산1: 선언
    cnt = 0
    
    # 계산2: 최소 변경 개수
    change = [min(ord(n) - ord('A') , ord('Z') - ord(n) + 1) for n in name]
    cnt += sum(change)
    
    # 계산3: 최소 이동 개수
    n = len(name)
    min_move = n - 1
    for i in range(n):
        
        #1. 'AAA...' 길이가 있는 곳 다음까지 이동
        right = i + 1
        while right < n and name[right] == 'A':
            right += 1
            
        # 2. 그림 참조
        min_move = min(min_move, 
                       (2 * i) + (len(name) - right), 
                       (i) + (2 * (len(name) - right))
                      )
    
    cnt += min_move
    
    return cnt