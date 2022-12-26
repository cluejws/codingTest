line = list(input())
line_list = []

while line:
    alp = "".join(line)
    line_list.append(alp)    
    
    if len(line) == 1:
        break

    data = line.pop(0)
line_list = sorted(line_list)

for pr in line_list:
    print(pr)
    


