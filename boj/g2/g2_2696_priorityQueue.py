# 입력
import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # 입력
    n = int(input())
    arr = []
    for _ in range((n//10)+1):
        ip = list(map(int,input().split()))
        for ele in ip:
            arr.append(ele)

    # 계산1: 초기화
    print_list = [-1 for _ in range((n//2) + 1)]
    min_heap = []
    max_heap = []
    mid = arr[0]
    print_list[0] = mid

    # 계산2: 숫자 순회
    for i in range(1, n):
        data = arr[i]

        if i % 2 == 1:
            if mid < data:
                heapq.heappush(max_heap, (data))
            else:
                heapq.heappush(min_heap, -(data))
        else:
            if mid < data:
                    # 1. 기저 조건(출력)
                    if len(max_heap) < len(min_heap):
                        heapq.heappush(max_heap, (data))
                        print_list[(i//2)] = mid
                        continue
                    
                    # 2. 정렬
                    pop_data = heapq.heappop(max_heap)

                    sorted_data = sorted([mid, data, pop_data])
                    heapq.heappush(min_heap, -(sorted_data[0]))
                    mid = sorted_data[1]
                    heapq.heappush(max_heap, sorted_data[2])

                    # 3. 출력
                    print_list[(i//2)] = mid
            else:
                    # 1. 기저 조건(출력)
                    if len(min_heap) < len(max_heap):
                        heapq.heappush(min_heap, -(data))
                        print_list[(i//2)] = mid
                        continue

                    # 2. 정렬   
                    pop_data = -(heapq.heappop(min_heap))

                    sorted_data = sorted([mid, data, pop_data])
                    heapq.heappush(min_heap, -(sorted_data[0]))
                    mid = sorted_data[1]
                    heapq.heappush(max_heap, sorted_data[2])
                    
                    # 3. 출력
                    print_list[(i//2)] = mid

    # 출력
    print(len(print_list))
    for i in range(len(print_list)):
        print(print_list[i], end=' ')
        if i % 10 == 9: print()
    print()