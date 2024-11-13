import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = list(map(int,input().split()))

# 계산: 투포인터
# 같은 원소가 K개 이하로 들어있음
# 최장 연속 부분 수열
visited = [0 for _ in range(100000 + 1)]
res = 0
j = 0
visited[arr[j]] += 1
for i in range(n):
    
    # 계산1: j 최대 길이로 이동
    while j + 1 < n and visited[arr[j+1]] < k:
        visited[arr[j+1]] += 1
        j += 1
    
    # 계산2: 해당 값 할당
    res = max(res, j-i+1)
    
    # 계산3: i 이동 처리
    visited[arr[i]] -= 1
    
# 출력
print(res)