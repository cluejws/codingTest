import math

data_list = list(map(int,input().split(" ")))

not_x = data_list[0] == data_list[2] == data_list[4]
not_y = data_list[1] == data_list[3] == data_list[5]

if data_list[0] - data_list[2] !=0:
    check = ((data_list[1]-data_list[3])/(data_list[0] - data_list[2]) * (data_list[4] - data_list[0]) + data_list[1] == data_list[5])
elif data_list[0] - data_list[4] !=0:
    check = ((data_list[1]-data_list[5])/(data_list[0] - data_list[4]) * (data_list[2] - data_list[0]) + data_list[1] == data_list[3])
elif data_list[2] - data_list[4] !=0:
    check = ((data_list[3]-data_list[5])/(data_list[2] - data_list[4]) * (data_list[0] - data_list[2]) + data_list[3] == data_list[1])
else:
    check = False
    

if not_x or not_y:
    print(-1.0)
elif check:
    print(-1.0)
else:
    res_list = []

    # 경우1
    x_a = (data_list[0] + data_list[2]) / 2
    y_a = (data_list[1] + data_list[3]) / 2

    x_1 = 2 * x_a - data_list[4]
    y_1 = 2 * y_a - data_list[5]

    res1_a_x = x_1 - data_list[0] 
    res1_a_y = y_1 - data_list[1]
    res1_a = res1_a_x * res1_a_x +  res1_a_y * res1_a_y
    res1_a = math.sqrt(res1_a)

    res2_a_x = x_1 - data_list[2]
    res2_a_y = y_1 - data_list[3]
    res2_a = res2_a_x * res2_a_x + res2_a_y * res2_a_y 
    res2_a = math.sqrt(res2_a)
    
    res_a = 2 * (res1_a + res2_a)
    res_list.append(res_a)

    # 경우2
    x_b = (data_list[0] + data_list[4]) / 2
    y_b = (data_list[1] + data_list[5]) / 2

    x_2 = 2 * x_b - data_list[2]
    y_2 = 2 * y_b - data_list[3]


    res1_b_x = x_2 - data_list[0] 
    res1_b_y = y_2 - data_list[1]
    res1_b = res1_b_x * res1_b_x +  res1_b_y * res1_b_y
    res1_b = math.sqrt(res1_b)

    res2_b_x = x_2 - data_list[4]
    res2_b_y = y_2 - data_list[5]
    res2_b = res2_b_x * res2_b_x + res2_b_y * res2_b_y 
    res2_b = math.sqrt(res2_b)

    res_b = 2 * (res1_b + res2_b)
    res_list.append(res_b)

    # 경우3
    x_c = (data_list[2] + data_list[4]) / 2
    y_c = (data_list[3] + data_list[5]) / 2

    x_3 = 2 * x_c - data_list[0]
    y_3 = 2 * y_c - data_list[1]

    res1_c_x = x_3 - data_list[2] 
    res1_c_y = y_3 - data_list[3]
    res1_c = res1_c_x * res1_c_x +  res1_c_y * res1_c_y
    res1_c = math.sqrt(res1_c)    

    res2_c_x = x_3 - data_list[4]
    res2_c_y = y_3 - data_list[5]
    res2_c = res2_c_x * res2_c_x + res2_c_y * res2_c_y 
    res2_c = math.sqrt(res2_c)

    res_c = 2 * (res1_c + res2_c)
    res_list.append(res_c)

    max = max(res_list)
    min = min(res_list)

    print(max - min)
