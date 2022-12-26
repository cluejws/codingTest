import sys
input = sys.stdin.readline

n,m = map(int,input().split())
str_book_arr = dict()
int_book_arr = dict()
for idx in range(n):
    info = input().rstrip()
    int_book_arr[str(idx+1)] = info
    str_book_arr[info] = str(idx+1)

problem = []
for _ in range(m):
    info = input().rstrip()
    
    if info.isdigit():
        print(int_book_arr[info])
    else:
        print(str_book_arr[info])