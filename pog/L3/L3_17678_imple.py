def getHMMinus(time):
    
    # 계산0: split 문자열
    hour_str, minute_str = time.split(':')
    hour = int(hour_str)
    minute = int(minute_str)
    
    # 계산1: -1분
    if minute - 1 < 0:
        hour -= 1
        minute = 59
    else:
        minute -= 1
    
    # 계산2: 문자열 HH:MM형식으로 만듬
    time = ''
    if hour >= 10:
        time += (str(hour) + ':')
    else:
        time += ('0' + str(hour)+ ':')
    
    if minute >= 10:
        time += (str(minute))
    else:
        time += ('0'+ str(minute))    
    
    return time


def getBusTable(n,t):
    bustable = ["09:00"]
    
    hour = 9
    minute = 0
    for _ in range(1, n):
        
        # 계산1
        minute += t
        if minute >= 60:
            hour += 1
            minute -= 60
        
        # 계산2: 문자열 HH:MM형식으로 만듬
        time = ''
        if hour >= 10:
            time += (str(hour) + ':')
        else:
            time += ('0' + str(hour)+ ':')
        
        if minute >= 10:
            time += (str(minute))
        else:
            time += ('0'+ str(minute))
        
        # 계산3: 배열 추가
        bustable.append(time)

    return bustable

def solution(n, t, m, timetable):
    
    res = ''
    
    # 계산1: timetable 정렬
    timetable.sort()
    
    # 계산2: 버스 09:00 총 n회 t분 간격 얻기
    bustable = getBusTable(n,t)
    
    # 계산3:
    i = 0
    for bus in bustable:
        
        # 계산3-1: cnt 계산
        cnt = 0
        while cnt < m and i < len(timetable) and timetable[i] <= bus:
            i += 1
            cnt += 1
        
        # 계산3-2: res 할당
        if cnt < m:
            res = bus                         # 버스도착시간에 도착
        else:
            res = getHMMinus(timetable[i-1])  # 크루 1분 전 시간에 도착
    
    return res    
