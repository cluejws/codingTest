import sys
input = sys.stdin.readline

t = int(input())
arr = []
for i in range(t):
    info = input().split()
    info.append(i)
    info_arr = [int(info[0]),info[1],info[2]]
    arr.append(info_arr)
    

arr.sort(key=lambda x: (x[0],x[2]))

for a in arr:
    print(a[0], a[1])