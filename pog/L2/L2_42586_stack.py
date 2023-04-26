def getResult(progresses, speeds):
    
    # 계산1: 배포까지 걸리는 시간 구하기
    n = len(progresses)
    time = [0 for _ in range(n)]
    for i in range(n):
        progress = progresses[i]
        speed = speeds[i]
        if (100 - progress) % speed == 0:
            time[i] = (100 - progress) // speed
        else:
            time[i] = ((100 - progress) // speed) + 1
    
    # 계산2: stack으로 판단
    res = []
    stack = [time[0]]
    cnt = 1
    for i in range(1, n):
        if stack[-1] < time[i]:
            stack.append(time[i])
            res.append(cnt)
            cnt = 1
        else:
            cnt += 1
    
    # 계산3: 끝 추가
    res.append(cnt)
        
    return res

def solution(progresses, speeds):
    res = getResult(progresses, speeds)
    return res