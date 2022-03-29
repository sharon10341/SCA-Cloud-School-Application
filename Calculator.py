print("Select an operation to perform:")
print ("1. for ADD")
print ("2. for SUBTRACT")
print ("3. for MULTIPLY")
print ("4. for DIVIDE")
operation = input()

if  operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is " + str(int(num1) + int(num2)))

elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The difference is " + str(int(num1) - int(num2)))


elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The multiplication is " + str(int(num1) * int(num2)))


elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The division is " + str(int(num1) / int(num2)))


else:
        print("Invalid entry")