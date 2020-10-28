try:
    operator = input("(+)(-)(*)(/) choose the operator: ")
    num1 = float(input("Please Enter The first number: "))
    num2 = float(input("Please Enter The second number: "))
    
    if operator == '+':
        result = num1 + num2
        print("Output: ", result)
    elif operator == '-':
        result = num1 - num2
        print("Output: ", result)
    elif operator == '*':
        result = num1 * num2
        print("output: ", result)
    elif operator == '/':
        try:
            if True:
                result = num1 / num2
                print(result)
        except ZeroDivisionError as err:
            print(err, " invalid number ")
    else:
        raise TypeError


except ValueError:
    print("Wrong input")
