def solution(k, room_number):
    
    result = getResult(k, room_number)
    return result

def getResult(k, room_number):
    
    res = []
    
    # 배정된 방(i) -> 사람(visited[i])
    visited = [-1 for _ in range(k+1)]
    
    # 계산1:
    # 비어있으면 -> 방 배정
    # 비어있지않으면 -> 원하는 방보다 번호가 크면서 / 비어있는 방 중 가장 번호가 작은 방을 배정
    for i in range(len(room_number)):
        if visited[room_number[i]] == -1:
            visited[room_number[i]] = 1
            res.append(room_number[i])
        else:
            min_room = findMinRoom(room_number[i], k, visited)
            visited[min_room] = 1
            res.append(min_room)

    return res
            
def findMinRoom(room_number, k, visited):
    
    # 계산2: 원하는 방보다 번호가 크면서 / 비어있는 방 중 가장 번호가 작은 방을 배정
    room = room_number + 1
    for i in range(room, k+1):
        if visited[i] == -1:
            room = i
            break
    
    return room