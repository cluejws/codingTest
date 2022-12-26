# 합/ 차 / 곱 / 나누기
def plus(data1, data2):
    return data1 + data2
def minus(data1, data2):
    return data1 - data2
def multiply(data1, data2):
    return data1 * data2
def div(data1, data2):
    return data1 / data2

# ord(문자 > 숫자), #chr(숫자 > 문자)
num = int(input())
line_list = list(input())

# A:값1 ...
dict_res = {}
for i in range(0,num):
    dict_res[ord("A")+i] = int(input())

# 결과 구하기
temp_list = []
for i in range(0,len(line_list)):
    data = line_list[i]

    if ord(data) in dict_res:
        temp_list.append(dict_res[ord(data)])
    else:
        data2 = temp_list.pop()
        data1 = temp_list.pop()
        res = 0
        if data == "+":
            res = plus(data1, data2)
        elif data == "-":
            res = minus(data1,data2)
        elif data == "*":
            res = multiply(data1,data2)
        elif data =="/":
            res = div(data1,data2)
        
        temp_list.append(res)
    
print("{:.2f}".format(temp_list[-1]))

