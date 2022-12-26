import sys
input = sys.stdin.readline

n,m = map(int,input().split())
book_arr = dict()
for idx in range(n):
    info = input().rstrip()
    book_arr[str(idx+1)] = info
    book_arr[info] = str(idx+1)

problem = []
for _ in range(m):
    info = input().rstrip()
    print(book_arr[info])