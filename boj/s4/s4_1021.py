def pop_data(data):
    global cnt

    # 계산0: top이 같으면 pop
    if data != cir_queue[0]:
        
        # 계산1: mid index
        mid = len(cir_queue) // 2
        
        # 계산2: data index
        data_index = 0
        for i in range(len(cir_queue)):
            if cir_queue[i] == data:
                data_index = i
        
        # 계산3: data index와 mid index 비교 후 움직임
        if data_index > mid:
            while data != cir_queue[0]:
                cnt += 1
                move_right()
        else:
            while data != cir_queue[0]:
                cnt += 1
                move_left()

    return cir_queue.popleft()

def move_left():
    data = cir_queue.popleft()
    cir_queue.append(data)

def move_right():
    data = cir_queue.pop()
    cir_queue.appendleft(data)

# 입력
from collections import deque

n,m = map(int,input().split())
pos_list = list(map(int,input().split()))

# 계산1: n만큼 길이 생성
cir_queue = deque([i+1 for i in range(n)])

# 계산2: 연산 통해 cnt 계산
cnt = 0
for pos in pos_list:
    pop_data(pos)

# 출력
print(cnt)