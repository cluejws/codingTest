num = int(input())

list_sum = []
result = 0
for data in range(1,num):
    data_1 = (data % (10)) // 1
    data_2 = (data % (100)) // 10
    data_3 = (data % (1000)) // 100
    data_4 = (data % (10000)) // 1000
    data_5 = (data % (100000)) // 10000
    data_6 = (data % (1000000)) // 100000

    check = (num == data + data_1 + data_2 + data_3 + data_4 + data_5 + data_6)
   
    if (check):
        list_sum.append(data)

if (len(list_sum)==0):
    print(0)
else:
    print(list_sum[0])

