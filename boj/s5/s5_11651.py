import sys
input = sys.stdin.readline

n = int(input())
data_list = []
for _ in range(n):
    data_list.append(list(map(int,input().split())))
    
data_list.sort(key=lambda x: (x[1],x[0]))
for data in data_list:
    print(data[0], data[1])