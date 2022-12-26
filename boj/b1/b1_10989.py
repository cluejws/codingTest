import sys

input = sys.stdin.readline

n = int(input())
cnt_arr = [0 for _ in range(10001)] 
for i in range(n):
    cnt_arr[int(input())] += 1    

for cnt in range(1,10001):
    if cnt_arr[cnt] > 0:
        for _ in range(cnt_arr[cnt]):
            print(cnt)

    
    