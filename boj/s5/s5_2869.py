import sys
input = sys.stdin.readline

a,b,v = map(int,input().split())

# a*day - b(day -1) = v
# (a-b)day = v-b
# day = (v-b)/(a-b) 
day = (v-b)/(a-b)
if int(day) == day:
    print(int(day))
else:
    print(int(day)+1)
    