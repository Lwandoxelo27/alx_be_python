# Prompt for User Input
num1 = float(input("Ebter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform the Calculation using Match Case
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed!")
            exit()
    case _=
        print("Error: Invalid operation!")
        exit()

# Output the Result
print(f"The result of {num1} {operation} {num2} is {result}")