num_list = list(map(int,input().split(" ")))

input_list = []
for i in range(0,num_list[0]):
    input_list.append([])
    input_person = input()
    for data in input_person:
        input_list[i].append(data)

# 행
count_a = 0
for i in range(0, num_list[0]):
    if "X" not in input_list[i]:
        count_a +=1
        
# 열
count_b = 0
for j in range(0,num_list[1]):

    temp_count = 0

    # 열 중에 X가 하나라도 있을 시 temp_count = 0
    # 열 중에 x가 하나라도 없을 시 temp_count != 0
    for i in range(0,num_list[0]):
        if input_list[i][j] == "X":
            temp_count = 0
            break
        else:
            temp_count += 1 

    if temp_count != 0:
        count_b += 1

# 최대값으로 경비원 배정시 최소값은 자동으로 경비원 배정
print(max(count_a,count_b))
