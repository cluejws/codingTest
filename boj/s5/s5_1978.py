from math import floor

def find(x):
    
    if x == 1:
        return False

    for i in range(2,floor(x**(1/2)+1)):
        if x % i == 0:
            return False

    return True

num = int(input())
num_list = list(map(int,input().split(" ")))
res_list = []

for n in num_list:
    if find(n):
        res_list.append(n)

print(len(res_list))
