a,b,c,d = map(int, input().split(" "))

res = min(a,b,abs(a-c),abs(b-d))
print(res)