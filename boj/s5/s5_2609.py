data = list(map(int,input().split(" ")))

min = min(data[0],data[1])
max_res = 1

for i in reversed(range(1,min+1)):
    if data[0] % i == 0 and data[1] % i == 0:
        max_res = max_res * i
        data[0] = data[0] // i
        data[1] = data[1] // i

print(max_res)
print(max_res * data[0] * data[1])

#####################################################
# 유클리드 호제법

def Euclidean(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

data = list(map(int,input().split(" ")))

max_res = Euclidean(data[0],data[1])

data[0] = data[0] // max_res
data[1] = data[1] // max_res

print(max_res)
print(max_res * data[0]  * data[1])

