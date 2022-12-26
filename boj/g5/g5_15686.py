import sys, math
input = sys.stdin.readline

def dfs(cnt,next,remove):

    # 기저조건1: 아예 치킨집이 없으면 안됨
    if len(ch_house) - remove == 0:
        return
    
    # 기저조건2: 치킨집 뺄 만큼 뺐는지? 후 할당
    global res
    if len(ch_house) - remove <= m:
        #print(f"치킨거리:{cnt} 치킨집수:{len(ch_house)-remove}")
        if res > cnt:
            res = cnt
        return
 
    # 완전탐색
    for i in range(next, len(ch_house)):
        
        ch_x, ch_y = ch_house[i]
        
        graph[ch_x][ch_y] = 0
        dfs(getChicken(), i+1, remove+1)
        graph[ch_x][ch_y] = 2


# 집-치킨집 거리 얻기
def getDistance(x,y, cx,cy): # 집(x,y), 치킨집(cx,cy)
    return abs(x-cx) + abs(y-cy)
    
# 치킨거리 얻기
def getChicken():
    
    # dfs할때 마다 집, 치킨집 얻기
    temp_house = []
    temp_ch_house = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                temp_ch_house.append((i,j))
            elif graph[i][j] == 1:
                temp_house.append((i,j))
    
    
    all_dist = 0
    
    for h in temp_house:
        
        min_dist = math.inf
        
        for ch in temp_ch_house:
            
            h_x, h_y = h
            ch_x, ch_y = ch
            
            dist = getDistance(h_x,h_y, ch_x, ch_y)
            if min_dist > dist:
                min_dist = dist
        
        all_dist = all_dist + min_dist
    
    return all_dist

# 입력
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

# 치킨집 후보군 얻기
ch_house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            ch_house.append((i,j))

# 계산
res = math.inf
dfs(getChicken(),0,0) #cnt, next, remove

# 출력
print(res)