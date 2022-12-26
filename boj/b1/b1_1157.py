str_input = input()
str_input = str_input.upper()


dict_count = {}

# 나온 글자 수 세기
for alp in str_input:
    list_keys = list(dict_count.keys())
    
    if (alp in list_keys):
        dict_count[alp] += 1
    else:
        dict_count[alp] = 1


# count가 1인, 즉 최대값이 오로지 하나일때만 출력
max = 0
count = 1
max_alp = ""
for key in dict_count:
    if(dict_count[key] > max):
        max = dict_count[key]
        max_alp = key
        count = 1
    elif(dict_count[key] == max):
        count += 1

if count == 1:
    print(max_alp)
else:
    print("?")