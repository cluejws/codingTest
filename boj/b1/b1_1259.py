while True:
    
    str_input = input()
    if(str_input == "0"):
        break
    
    check = True
    for index in range(0,len(str_input)):
        if(str_input[index]!=str_input[-(index)-1]):
            check = False
            break

    if check:
        print("yes")
    else:
        print("no")