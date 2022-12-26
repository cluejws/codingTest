# insert = O(N^2)

result = list(input())

test_case = int(input())

cursor = len(result) 
for i in range(0,test_case):
    
    line = input()

    if "L" in line:

        if cursor == 0:
            pass
        else:
            cursor -= 1

    elif "D" in line:
        
        if cursor == len(result):
            pass
        else:
            cursor += 1

    elif "B" in line:

        if cursor == 0:
            pass
        else:
            result.pop(cursor-1)
            cursor -= 1
    elif "P" in line:
        
        if cursor == len(result):
            result.append(line[2])
            cursor += 1
        else:
            result.insert(cursor, line[2])
            cursor +=1

print("".join(result))

