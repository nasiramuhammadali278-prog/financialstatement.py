print("This is our calculator")
a = ("Plus", "Minus", "Multiply", "Division")
print(a)
operation = input("Which operation do you want to perform? ")

if operation == "Plus":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The answer is: ", num1 + num2)
elif operation == "Minus":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("The answer is: ", num1 - num2)
elif operation == "Multiply":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("The answer is: ", num1 * num2)
elif operation == "Division":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("The answer is: ", num1 / num2)
     
m = ("yes")
l = ("no")
p = input("do you wish to continue calculating?")
print(p)

while p != l:
    a = ("Plus", "Minus", "Multiply", "Division")
    print(a)
    operation = input("Which operation do you want to perform: ")
    if operation == "Plus":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("The answer is: ", num1 + num2)
    elif operation == "Minus":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("The answer is: ", num1 - num2)
    elif operation == "Multiply":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("The answer is: ", num1 * num2)
    elif operation == "Division":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("The answer is: ", num1 / num2)
    elif p == l:
        print("Thank you for using our calculator")
        break

     
