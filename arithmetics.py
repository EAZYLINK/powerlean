num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter math operation: ")

print(str(num1) + " " + operation + " " + str(num2) + " = " + str(eval(f"{num1} {operation} {num2}")))