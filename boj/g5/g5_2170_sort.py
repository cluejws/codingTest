import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

# 계산1: 정렬
arr.sort(key=lambda x: (x[0], x[1]))

# 계산2: 하나씩 꺼내서 포인터 이동
start = arr[0][0]
end = arr[0][1]
res = end - start
for i in range(1, len(arr)):
    
    next_start, next_end = arr[i]

    if next_start > end:
        
        res = res + (next_end - end) - (next_start - end)
        
        start = next_start
        end = next_end
        
    else:
        
        if next_end >= end:
                    
            res = res + (next_end - end)
        
            start = next_start
            end = next_end
        else:
            pass
    
# 출력
print(res)