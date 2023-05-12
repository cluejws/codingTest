def getResult(line):
    
    # 1. split(공백)
    split_line = line.split()
    s, t = split_line[1], split_line[2]
    
    # 2. res_s
    res_s = 0
    split_s = s.split(':')
    res_s += float(split_s[0]) * 60 * 60
    res_s += float(split_s[1]) * 60
    res_s += float(split_s[2])
    
    # 3. res_t
    res_t = 0
    res_t = float(t.rstrip('s'))
    
    return (res_s, res_t)
    

def solution(lines):
    
    # 계산1: 시간 테이블 생성
    tables = []
    for line in lines:
        s, t = getResult(line)
        if (s-t + 0.001) <= 0:
            tables.append((0, s))
        else:
            tables.append((s - t + 0.001, s))

    # 계산2: (현재 지점부터 1초 동안) 겹치는 최대 개수 얻기
    n = len(tables)
    
    max_cnt = 0
    for i in range(n):
        
        # 1.
        cur_s, cur_e = tables[i]
        
        # 2. 다음 시작(지점) < 현재 끝(지점) + 1초 
        cnt = 1
        for j in range(i + 1, n):
            next_s, next_e = tables[j]
            if next_s < cur_e + 1:
                cnt += 1

        # 3.
        max_cnt = max(max_cnt, cnt)
        
    return max_cnt