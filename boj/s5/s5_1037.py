num = int(input())

data_list = list(map(int,input().split(" ")))

r_data_list = sorted(data_list)

res = r_data_list[0] * r_data_list[-1] 
print(res)