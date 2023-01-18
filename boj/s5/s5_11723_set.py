m = int(input())

group = set()
for _ in range(m):
    
    line = input().split()
    if len(line) == 1:
        if line[0] == 'all':
            group = set([i for i in range(1, 21)])
        elif line[0] == 'empty':
            group = set([])
        continue
    
    if line[0] == 'add':
        group.add(int(line[1]))
    elif line[0] == 'remove':
        if int(line[1]) in group:
            group.remove(int(line[1]))
    elif line[0] == 'check':
        if int(line[1]) in group:
            print(1)
        else:
            print(0)
    elif line[0] == 'toggle':
        if int(line[1]) in group:
            group.remove(int(line[1]))
        else:
            group.add(int(line[1]))
