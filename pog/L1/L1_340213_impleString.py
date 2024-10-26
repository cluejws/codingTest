def getSecond(time):
    second = list(map(int,time.split(":")))
    return second[0] * 60 + second[1]

def getTime(second):
    # 1.
    minute = second // 60
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)
    
    # 2.
    second = second % 60
    if second < 10:
        second = "0" + str(second)
    else:
        second = str(second)
    
    return minute + ":" + second

def checkOpening(pos, op_start, op_end):
    return op_start <= pos <= op_end

def solution(video_len, pos, op_start, op_end, commands):
    # 계산1: 오프닝 체크
    if checkOpening(pos, op_start, op_end):
        pos = op_end
    
    # 계산2: 순회
    for command in commands:
        # 2-1: 명령어
        if command == 'prev':
            # 10초 미만
            if getSecond(pos) < 10:
                pos = "00:00"
            else:
                pos = getTime(getSecond(pos) - 10)
            
        elif command == 'next':
            # 남은 시간 10초 미만
            if getSecond(pos) + 10 > getSecond(video_len):
                pos = video_len
            else:
                pos = getTime(getSecond(pos) + 10)
        
        # 2-2: 오프닝 체크
        if checkOpening(pos, op_start, op_end):
            pos = op_end
        
    return pos