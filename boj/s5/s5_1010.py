# 10C5로 이용
num = int(input())

for i in range(0,num):
    int_list = list(map(int,input().split(" ")))
    
    left = int_list[0]
    right = int_list[1]
    
    if(left < right):
        
        result = 1
        temp = right
        for j in range(1,left+1):
            result = result * temp
            temp -= 1
        
        div =1
        div_temp = left
        for j in range(1,left+1):
            div = div * div_temp
            div_temp -= 1

        print(result//div)


    elif(left == right):
        print(1)

