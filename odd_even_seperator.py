def odd_even_seperator():
    print("This is the odd even number seperator.")
    numbers = []
    odd_numbers = []
    even_numbers = []
    while True:
        print("To [E]xit")
        try:
            original_numbers = input("Enter a number: ")
            if original_numbers.lower() == "e":
                break
            else:
                original_numbers = original_numbers.strip().replace(" ", "").split(",")
                numbers = []
                if len(numbers) >= len(original_numbers):
                    break
                else:
                    for number in original_numbers:
                        number = int(number)
                        numbers.append(number)
                for number in numbers:
                    check_number = number % 2
                    if check_number == 0:
                        even_numbers.append(number)
                    else:
                        odd_numbers.append(number)
                print(f"Here are the even numbers: {even_numbers}")
                print(f"Here are the odd numbers: {odd_numbers}")
        except ValueError:
            print("Enter integers please.")
    print("Even-odd number seperator exited.")


odd_even_seperator()
