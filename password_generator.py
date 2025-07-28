def password_generator():
    import random
    print("This is the password generator.")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ["@", "!", "#", "&", "$", "%", "*", "_", "-",
               "(", ")", "+", "=", "[", "]", "{", "}", ";", ":", "'", ",", "<", ">", "?", "/", "|",]

    while True:
        print("To [E]xit")
        password = []
        num_of_letters = input("Enter amount of letters to include: ")
        if num_of_letters.lower().strip() == "e":
            break
        num_of_digits = input("Enter amount of numbers to include: ")
        if num_of_digits.lower().strip() == "e":
            break
        num_of_symbols = input("Enter number of symbols to include: ")
        if num_of_symbols.lower().strip() == "e":
            break
        try:
            num_of_letters = int(num_of_letters)
            num_of_digits = int(num_of_digits)
            num_of_symbols = int(num_of_symbols)
            if num_of_letters < 1:
                print("Num of letters to less.")
            if num_of_digits < 1:
                print("Num of digits to less.")
            if num_of_symbols < 1:
                print("Num of symbols to less.")
            for i in range(num_of_letters):
                letter = random.choice(letters)
                password.append(letter)
            for i in range(num_of_digits):
                digit = random.choice(digits)
                password.append(digit)
            for i in range(num_of_symbols):
                symbol = random.choice(symbols)
                password.append(symbol)
            random.shuffle(password)
            if len(password) < 8:
                print("Length of password too short.")
            else:
                print("Your new strong password is: ", "".join(password))
        except ValueError:
            print("Please enter an integer.")
    print("Password generator exited.")


password_generator()
