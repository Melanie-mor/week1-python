number1=input(int("Enter the first number: "))

operation=input("Enter the operation: ")

number2=input(int("Enter the second number: "))

if operation=="+":
    print(number1+number2)
elif operation=="-":
    print(number1-number2)
elif operation=="*":
    print(number1*number2)
elif operation=="/":
    print(number1/number2)
else:
    print("Invalid operation")
    

