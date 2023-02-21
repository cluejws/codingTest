# 입력
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = list(map(int,input().split()))

# 계산1: 차이 구하기
diff_arr = [0 for _ in range(n-1)]
for i in range(n-1):
    diff_arr[i] = arr[i+1] - arr[i]

# 계산2: 차이 정렬
diff_arr.sort(reverse=True)

# 계산3: k-1개 만큼 빼기 -> 해당 구간 지워진 것
diff_arr = diff_arr[k-1:]

# 출력
print(sum(diff_arr))