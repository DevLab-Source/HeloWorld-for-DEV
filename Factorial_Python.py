try:
    num = int(input("Enter an integer: "))
    factorial = 1
    if num < 0:
        print("Error! Factorial of a negative number doesn't exist")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
         factorial = factorial*i
        print("Factorial of",num,"is :",factorial)
except ValueError:
     print("Wrong input")