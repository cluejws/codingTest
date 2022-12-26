import sys
input = sys.stdin.readline

l = int(input())
st = input()

res = 0
for i in range(l):
    temp = ord(st[i]) - ord("a") + 1
    res += temp * (31 ** (i))
print(res % 1234567891)