def getTime(time):
    
    a,b = time.split(":")
    return int(a) * 60 + int(b)

def getClock(time):
    
    res = ""
    
    a = time // 60
    b = time % 60
    if a // 10 == 0 and b // 10 == 0:
        res = "0" + str(a) + ":" + "0" + str(b)
    elif a // 10 == 0:
        res = "0" + str(a) + ":" + str(b)
    elif b // 10 == 0:
        res = str(a) + ":" + "0" + str(b)
    else:
        res = str(a) + ":" + str(b)
        
    return res
    
def solution(n, t, m, timetable):
    
    # 계산1: 시간 정렬
    timetable.sort()
    
    # 계산2
    maxTime = 0
    
    cnt = 0
    start = 60 * 9
    id = 0
    while cnt < n:
        
        # 1. 해당 출발 시간 -> id 부터 순회
        person = []
        for i in range(id, len(timetable)):
            time = getTime(timetable[i])
            if len(person) < m and time <= start:
                person.append((time, i))
    
        # 2. 최대 출발 시간
        if len(person) > 0:
            if len(person) == m:
                maxTime = max(maxTime, person[-1][0] - 1)
            else:
                maxTime = max(maxTime, start)
        else:
            maxTime = max(maxTime, start)
        
        # 3. 다음 준비 
        cnt += 1
        start += t
        if len(person) > 0:
            id = person[-1][1] + 1
    
    return getClock(maxTime)