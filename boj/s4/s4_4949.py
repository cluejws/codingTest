while True:
    line = input()
    if line ==".":
        break
    
    stack = []
    check_break = True
    for alp in line:
        if alp == "(":
            stack.append(alp)
        elif alp == "[":
            stack.append(alp)
        elif alp == ")":
            if len(stack) != 0:
                data = stack.pop()
                if data =="(":
                    pass
                else:
                    check_break = False
                    break
            else:
                check_break = False
                break
        elif alp == "]":
            if len(stack) != 0:
                data = stack.pop()
                if data == "[":
                    pass
                else:
                    check_break = False
                    break
            else:
                check_break = False
                break
        

    if check_break and len(stack) == 0:
        print("yes")
    else:
        print("no")


