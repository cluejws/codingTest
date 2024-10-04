def getPoints(edges):
    points = set()
    for edge in edges:
        a, b = list(map(int, edge))
        points.add(a)
        points.add(b)
    
    return points

def solution(edges):
    # 계산1: 정점
    points = getPoints(edges) 

    # 계산2: 해당 정점, in/out 수
    n = max(list(points))
    in_cnts = [0 for _ in range(n)]
    out_cnts = [0 for _ in range(n)]
    for a, b in edges:
        out_cnts[a-1] += 1
        in_cnts[b-1] += 1
    
    # 계산3
    """
    생성노드: 그래프 2개 이상 →  in x / out 2개 이상
    막대그래프: → in 1개 이상 / out x
    8자그래프: → in 2개 이상 / out 2개
    도넛그래프: → out[생성노드] - 막대그래프 - 8자그래프
    """
    created_node = -1
    stick_cnt = 0
    eight_cnt = 0
    dnt_cnt = 0
    for idx in range(n):
        if in_cnts[idx] == 0 and out_cnts[idx] >= 2:
            created_node = idx
        elif in_cnts[idx] >= 1 and out_cnts[idx] == 0:
            stick_cnt += 1
        elif in_cnts[idx] >= 2 and out_cnts[idx] >= 2:
            eight_cnt += 1
    
    dnt_cnt = out_cnts[created_node] - stick_cnt - eight_cnt
    
    # 출력
    return [created_node+1, dnt_cnt, stick_cnt, eight_cnt]