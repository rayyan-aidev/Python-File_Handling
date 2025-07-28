def factorial_func():

    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return factorial(n-1) * n

    while True:
        try:
            n = int(
                input("Enter a non-negative integer to get factorial (or -1 to exit): "))
            if n < 0:
                if n == -1:
                    print("Exiting the program.")
                    break
                else:
                    print("Please enter a non-negative integer.")
            else:
                print(
                    f"The factorial of {n} is: {factorial(n)}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


factorial_func()
