# 계산4: 내구도 판단
def getZero():
    zero_cnt = 0
    for i in range(len(queue)):
        if queue[i] == 0:
            zero_cnt += 1
    return zero_cnt

# 계산1: 벨트,로봇 같이 움직임 / 뺌
def moveBelt():
    pop_data = queue.pop()
    queue.appendleft(pop_data)

    pop_robot = robot.pop()
    robot.appendleft(pop_robot)

    # n-1(문제에서 n)위치에 로봇이면 뺌
    if robot[n-1] == True:

        robot[n-1] = False

# 계산2: 로봇 이동 / 뺌
def moveRobot():

    # 가장 먼저 올라간 로봇부터 움직임
    # n-2부터 n-1로 움직임
    # n-2~0
    for i in range(n-2, -1, -1):
        if robot[i+1] == True:
            pass
        else:
            if queue[i+1] >= 1 and robot[i] == True:
                robot[i+1] = robot[i]
                robot[i] = False
                queue[i+1] -= 1

                # n-1(문제에서 n)위치에 로봇이면 뺌
                if robot[n-1] == True:
                    robot[n-1] = False
            else:
                pass

# 계산3: 로봇 올림
def setRobot():
    if queue[0] >= 1:
        robot[0] = True
        queue[0] -= 1
    else:
        pass

# 입력
from collections import deque

n, k = map(int,input().split())
queue = deque(map(int,input().split()))
robot = deque([False for _ in range(2*n)])

# 계산1: 벨트,로봇 같이 움직임 / 뺌
# 계산2: 로봇 이동 / 뺌
# 계산3: 로봇 올림
# 계산4: 내구도 판단
cnt = 0
while True:
    cnt += 1

    # 계산1: 벨트,로봇 같이 움직임 / 뺌
    moveBelt()

    # 계산2: 로봇 이동 / 뺌
    moveRobot()

    # 계산3: 로봇 올림
    setRobot()

    # 계산4: 내구도 판단
    if getZero() >= k:
        break

# 출력
print(cnt)