num = int(input())

dict_len = {}
for i in range(0,num):
    line = input()

    if len(line) in dict_len:
        if line not in dict_len[len(line)]:
            dict_len[len(line)].append(line)
    else:
        dict_len[len(line)] = [line]
for i in sorted(list(dict_len.keys())):
    for j in sorted(dict_len[i]):
        print(j)
