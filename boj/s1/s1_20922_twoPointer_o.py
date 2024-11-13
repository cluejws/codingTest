# 입력
n, k = map(int,input().split())
arr = list(map(int,input().split()))

# 계산: 투포인터
max_res = 0
visited = [0 for _ in range(100000 + 1)]
j = 0

visited[arr[0]] += 1
for i in range(n):
    
    # 1. j를 같은 숫자가 k개가 될 때까지, 초과해서(=k) 이동
    while j + 1 < n and visited[arr[j + 1]] < k:
        visited[arr[j + 1]] += 1
        j += 1
    
    # 2. 최대 길이 할당
    max_res = max(max_res, j - i + 1)
    
    # 3. 다음 준비
    visited[arr[i]] -= 1
    
# 출력
print(max_res)