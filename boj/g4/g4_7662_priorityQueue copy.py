# 입력
import heapq

t = int(input())
for _ in range(t):
    
    # 힙
    min_arr = []
    max_arr = []
    visited = [False for _ in range(1000000 + 1)]
    
    k = int(input())
        
    # 계산1: 입력 후 판별
    for i in range(k):

        str_line, int_line = input().split()
        number = int(int_line)
        
        if str_line == 'I':
            heapq.heappush(max_arr, (-number, i))
            heapq.heappush(min_arr, (number, i))
            visited[i] = True
            
        elif str_line == 'D':
            if int_line == '1':
                
                while len(max_arr) > 0 and visited[max_arr[0][1]] == False:
                    heapq.heappop(max_arr)
            
                if len(max_arr) > 0:
                    data, index = heapq.heappop(max_arr)
                    visited[index] = False
                
            
            elif int_line == '-1':
                
                while len(min_arr) > 0 and visited[min_arr[0][1]] == False:
                    heapq.heappop(min_arr)
                
                if len(min_arr) > 0:
                    data, index = heapq.heappop(min_arr)
                    visited[index] = False
                
                   
    # 계산2: 방문처리 적용
    while len(max_arr) > 0 and visited[max_arr[0][1]] == False:
        heapq.heappop(max_arr)
    
    while len(min_arr) > 0 and visited[min_arr[0][1]] == False:
        heapq.heappop(min_arr)

                
    # 출력
    if len(max_arr) == 0:
        print('EMPTY')
    else:
        print(-heapq.heappop(max_arr)[0], heapq.heappop(min_arr)[0])