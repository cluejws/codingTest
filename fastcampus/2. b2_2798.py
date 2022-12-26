int1_list = list(map(int,input().split(" "))) # 카드개수, 최대정수
int2_list = list(map(int,input().split(" "))) # 카드들

temp_list = []
temp = 0
max = 0

for i in range(0,len(int2_list)):
    temp += int2_list[i]

    for j in range(i+1,len(int2_list)):
        temp += int2_list[j]

        for k in range(j+1, len(int2_list)):
            temp += int2_list[k]
            temp_list.append(temp)
            temp -= int2_list[k]

        temp -= int2_list[j]

    temp -= int2_list[i]

for data in temp_list:
    if(data > int1_list[1]):
        pass
    else:
        if(max <= data):
            max = data

print(max)
