def calculator():
    import math
    while True:
        print("Type e to exit")
        print("Note: In single-number operations only first number will be used")
        operator = input(
            "Choose from the following:\n1=addition,2=subtraction, 3=division, 4=multiplication, 5=absolute value, 6=square, 7=square root, 8=round, 9=max, 10=min, 11=exponent: ")
        if operator.lower() == "e":
            break
        num1 = input("Enter the first number: ")
        if num1.lower() == "e":
            break
        num2 = input("Enter second number: ")
        if num2.lower() == "e":
            break
        try:
            num1 = float(num1)
            num2 = float(num2)
            if operator == "1":
                result = num1 + num2
            elif operator == "2":
                result = num1 - num2
            elif operator == "3":
                if num2 == 0:
                    result = "Cannot divide by zero"
                else:
                    result = num1 / num2
            elif operator == "4":
                result = num1 * num2
            elif operator == "5":
                result = abs(num1)
            elif operator == "6":
                result = num1*num1
            elif operator == "7":
                result = math.sqrt(num1)
            elif operator == "8":
                result = round(num1)
            elif operator == "9":
                result = max(num1, num2)
            elif operator == "10":
                result = min(num1, num2)
            elif operator == "11":
                result = pow(num1, num2)
            else:
                result = "Invalid operator"
            print(f"Result: {result}")
        except ValueError:
            print("Please enter valid numbers in numeric form")
    print("Calculator exited")


calculator()
