# 입력
n = int(input().rstrip())
buildings = list(map(int,input().rstrip().split()))

# cnt[i]: i위치에서 보이는 건물 개수
# near[i][0]: i위치에서 가장 가까운 건물 index
# near[i][1]: i위치에서 가장 가까운 건물 거리
cnt = [0]*(n+1)
near = [[int(1e9),int(1e9)] for _ in range(n+1)]

# 계산: 왼쪽
# stack: 이전 idx의 건물에서 보이는 건물들 모음
stack = []
for idx, building in enumerate(buildings):
    
    # 계산1: 비교해서 제거
    # (1) (이전 idx의 건물)에서 보이는 건물들 모음 > 0 
    # (2) (이전 idx의 건물)<->(현재 idx의 건물 = building) 높이 비교해서 같거나 작을때
    while len(stack)>0 and stack[-1][1] <= building:
        stack.pop()
    
    # 계산2: cnt 할당
    # (1) (현재 idx의 건물)에서 보이는 건물들 모음
    cnt[idx+1] += len(stack)
    
    # 계산3: near 할당
    # (현재 idx의 건물)에서 보이는 건물들 모음
    # (가장 가까운 거리)<->(near[i][1]: i위치에서 가장 가까운 건물 거리) 높이 비교
    if len(stack) > 0:
        min_dist = abs(stack[-1][0] - (idx+1))
        if min_dist < near[idx+1][1]:
            near[idx+1][0] = stack[-1][0]
            near[idx+1][1] = min_dist
        elif min_dist == near[idx+1][1] and stack[-1][0] < near[idx+1][0]:
            near[idx+1][0] = stack[-1][0]
    
    # 계산4: 현재 idx의 건물을 (이전 idx의 건물)로 처리  
    stack.append([idx+1,building])

# 계산: 오른쪽
stack = []
for idx, building in reversed(list(enumerate(buildings))):
    
    # 계산1: 비교해서 제거
    # (1) (이전 idx의 건물)에서 보이는 건물들 모음 > 0 
    # (2) (이전 idx의 건물)<->(현재 idx의 건물 = building) 높이 비교해서 같거나 작을때
    while len(stack)>0 and stack[-1][1] <= building:
        stack.pop()
    
    # 계산2: cnt 할당
    # (1) (현재 idx의 건물)에서 보이는 건물들 모음
    cnt[idx+1] += len(stack)
    
    # 계산3: near 할당
    # (현재 idx의 건물)에서 보이는 건물들 모음
    # (가장 가까운 거리)<->(near[i][1]: i위치에서 가장 가까운 건물 거리) 높이 비교
    if len(stack) > 0:
        min_dist = abs(stack[-1][0] - (idx+1))
        if min_dist < near[idx+1][1]:
            near[idx+1][0] = stack[-1][0]
            near[idx+1][1] = min_dist
        elif min_dist == near[idx+1][1] and stack[-1][0] < near[idx+1][0]:
            near[idx+1][0] = stack[-1][0]
    
    # 계산4: 현재 idx의 건물을 (이전 idx의 건물)로 처리  
    stack.append([idx+1,building])

# 출력
for i in range(1,n+1):
    if cnt[i]>0:
        print(str(cnt[i])+' '+str(near[i][0]))
    else:
        print(0)