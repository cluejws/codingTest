int_list = list(map(int, input().split(" ")))

res_list = []
for x in range(0,len(int_list)):
    for y in range(x+1, len(int_list)):
        for z in range(y+1, len(int_list)):
            a = int_list[x]
            b = int_list[y]
            c = int_list[z]

            result = a
            while True:
                
                div_a = result // a
                check1 = (a * div_a == result)

                div_b = result // b
                check2 = (b * div_b == result)

                div_c = result // c
                check3 = (c * div_c == result)

                if check1 and check2 and check3:
                    res_list.append(result)
                    break
                else:
                    result += 1
print(min(res_list))