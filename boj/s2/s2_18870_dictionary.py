import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

# 계산1: 반복되는 숫자 줄이고 정렬
sorted_arr = sorted(list(set(arr)), key=lambda x: -x)
        
# 계산2: 개수 구하기
dict_arr = {}
for i in range(len(sorted_arr)):
    
    data = sorted_arr[i]
    if data not in dict_arr:
        dict_arr[data] = len(sorted_arr) - i - 1

# 출력
print_arr = [0 for _ in range(n)]
for i in range(len(arr)):
    print_arr[i] = dict_arr[arr[i]]

print(*print_arr) 