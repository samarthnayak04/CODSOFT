def simple_calculator():
    print("Welcome to the Simple Calculator!")


    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))


    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")

    operation_choice = input("Enter the number corresponding to your choice: ")

    if operation_choice == '1':
        result = num1 + num2
        operation = "Addition"
    elif operation_choice == '2':
        result = num1 - num2
        operation = "Subtraction"
    elif operation_choice == '3':
        result = num1 * num2
        operation = "Multiplication"
    elif operation_choice == '4':
        if num2 != 0:
            result = num1 / num2
            operation = "Division"
        else:
            print("Error: Cannot divide by zero!")
            return
    else:
        print("Invalid choice! Please choose a number from 1 to 4.")
        return

    print(f"\n{operation} Result: {num1} {operation_choice} {num2} = {result}")


