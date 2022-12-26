N, check = map(int,input().split(" "))

data_list = [i for i in range(1,N+1) ]
search = 0
print_list = []
for i in range(0,N):

    search += check -1
    search = search % len(data_list)

    data = data_list.pop(search)
    print_list.append(data)

print("<"+ ', '.join(str(i) for i in print_list)+ ">")