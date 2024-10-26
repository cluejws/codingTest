def solution(points, routes):
    # 초기화
    x = len(routes)
    dict_robot = {}
    for robot_idx in range(x):
        dict_robot[robot_idx] = []
        
    # 로봇 경로 기록(x, y)
    for robot_idx in range(x):
        # 1. 초기화 경로 기록
        route = routes[robot_idx]
        init_x, init_y = points[(route[0]) - 1]
        dict_robot[robot_idx].append((init_x, init_y))
        
        # 2. 경로 기록
        m = len(route)
        for point_idx in range(1, m):
            # 1.
            sx, sy = points[(route[point_idx-1])-1]
            ex, ey = points[(route[point_idx])-1]
            
            # 2. 최단 경로
            # r 좌표 이동(우선순위 높)
            if sx < ex:
                while (sx + 1) <= ex:
                    dict_robot[robot_idx].append((sx+1, sy))
                    sx += 1
            elif sx > ex:
                while (sx - 1) >= ex:
                    dict_robot[robot_idx].append((sx-1, sy))
                    sx -= 1
            
            # c 좌표 이동(우선순위 낮)
            if sy < ey:
                while (sy + 1) <= ey:
                    dict_robot[robot_idx].append((ex, sy+1))
                    sy += 1
            elif sy > ey:
                while (sy - 1) >= ey:
                    dict_robot[robot_idx].append((ex, sy-1))
                    sy -= 1
        
    # 로봇 경로 시간 기록(x, y, robot_idx)
    dict_time = {}
    for robot_idx in dict_robot:
        robot_route = dict_robot[robot_idx]
        for time in range(len(robot_route)):
            x, y = robot_route[time]
            if time not in dict_time:
                dict_time[time] = set()
                dict_time[time].add((x, y, robot_idx))
            else:
                dict_time[time].add((x, y, robot_idx))

    # 충돌 개수
    cnt = 0
    for time in dict_time:
        # 1.
        dict_pos = {}
        
        # 2.
        set_pos = dict_time[time]
        for x, y, robot_idx in set_pos:
            if (x, y) not in dict_pos:
                dict_pos[(x, y)] = 1
            else:
                dict_pos[(x, y)] += 1
        
        # 3.
        for x, y in dict_pos:
            if dict_pos[(x, y)] > 1:
                cnt += 1
    
    return cnt