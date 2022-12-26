decryption = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}


t = int(input())
for tc in range(t):
    n,m = map(int,input().split())
    arr = [input() for _ in range(n)]

    code = ""
    for i in range(n):
        for j in range(m-1, -1, -1):
            if arr[i][j] == '1':
                code += arr[i][j-55 : j+1]

    dcode = []
    start, end = 0,7
    for i in range(8):
        dcode.append(decryption[code[start:end]])
        start += 7
        end += 7

    if ((dcode[0] + dcode[2] + dcode[4] + dcode[6]) * 3 + dcode[1] + dcode[3] + dcode[5] + dcode[7]) % 10 == 0:
        print('#{} {}'.format(tc, sum(dcode)))
    else:
        print('#{} {}'.format(tc, 0))
