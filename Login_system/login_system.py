import random
import os
import json
print("This is the login window.")


def password_make(password_choice):
    if password_choice == "1":
        password = []
        for i in range(random.randint(1, 5)):
            lower_letter = random.choice(lower_letters)
            password.append(lower_letter)
        for i in range(random.randint(1, 5)):
            upper_letter = random.choice(upper_letters)
            password.append(upper_letter)
        for i in range(random.randint(1, 5)):
            digit = random.choice(digits)
            password.append(digit)
        for i in range(random.randint(1, 2)):
            symbol = random.choice(symbols)
            password.append(symbol)
        random.shuffle(password)
        password = "".join(password)
    elif password_choice == "2":
        password = input("Enter your password: ")
        password = password_strength_check(password)
    else:
        print("Please enter correct action.")
        return None
    return password


def sign_up(username_choice):
    if username_choice == "1":
        username = []
        for i in range(random.randint(1, 5)):
            lower_letter = random.choice(lower_letters)
            username.append(lower_letter)
        for i in range(random.randint(1, 5)):
            upper_letter = random.choice(upper_letters)
            username.append(upper_letter)
        for i in range(random.randint(1, 5)):
            digit = random.choice(digits)
            username.append(digit)
        for i in range(random.randint(1, 5)):
            symbol = random.choice(symbols)
            username.append(symbol)
        random.shuffle(username)
        username = "".join(username)
    elif username_choice == "2":
        username = input("Enter your username: ")
    else:
        print("Please enter correct action.")
        return None
    return username


def password_strength_check(password):
    num_of_lower_letters = 0
    num_of_upper_letters = 0
    num_of_digits = 0
    num_of_symbols = 0
    for lower_letter in lower_letters:
        if lower_letter in password:
            num_of_lower_letters += 1
    for upper_letter in upper_letters:
        if upper_letter in password:
            num_of_upper_letters += 1
    for digit in digits:
        if digit in password:
            num_of_digits += 1
    for symbol in symbols:
        if symbol in password:
            num_of_symbols += 1
    if len(password) < 8:
        print("Password length too short.")
        return None
    elif num_of_lower_letters < 1:
        print("Include atleast one lowercase letter.")
        return None
    elif num_of_upper_letters < 1:
        print("Include atleast one uppercase character.")
        return None
    elif num_of_digits < 1:
        print("Include atleast one number.")
        return None
    elif num_of_symbols < 1:
        print("Include atleast one special character.")
        return None
    else:
        return password


lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ["@", "!", "#", "&", "$", "%", "*", "_", "-",
           "(", ")", "+", "=", "[", "]", "{", "}", ";", ":", "'", ",", "<", ">", "?", "/", "|",]
file_path = "File_Handling/Login_system/login_details.json"
user_details = {

}
while True:
    print("To [E]xit.")
    try:
        action = input(
            "1-Sign up\n2-Login\n3-Forgot password\n").lower().strip().replace(" ", "")
        if action == "e":
            break
        if action == "1":
            username_choice = input("1-Random username\n2-Type in username\n ")
            if username_choice.lower().strip() == "e":
                break
            username = sign_up(username_choice)
            if username is None:
                continue
            password_choice = input(
                "1-Random password\n2-Type in password\n ")
            if password_choice.lower().strip() == "e":
                break
            password = None
            while password is None:
                password = password_make(password_choice)
            password = password_strength_check(password)
            while password is None:
                password = password_make(password_choice)
                password = password_strength_check(password)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    json.dump({}, f)
            with open(file_path, "r") as f:
                try:
                    content = json.load(f)
                except Exception:
                    content = {}
                user_details = content
                while username in user_details:
                    print("Username not available.")
                    username_choice = input(
                        "1-Random username\n2-Type in username\n ")
                    if username_choice.lower().strip() == "e":
                        username = None
                        break
                    username = sign_up(username_choice)
                if username is None:
                    continue
                user_details[username] = password
            print(f"Your new username is: {username}")
            print(f"Your new password is: {password}")
            with open(file_path, "w") as f:
                json.dump(user_details, f, indent=2, sort_keys=True)
        elif action == "2":
            if not os.path.exists(file_path):
                print("No users registered yet.")
                continue
            with open(file_path, "r") as f:
                try:
                    content = json.load(f)
                except Exception:
                    content = {}
                typed_username = input(
                    "Enter your username: ").strip()
                if typed_username == "e":
                    break
                typed_password = input("Enter your password: ")
                if typed_password.lower().strip() == "e":
                    break
                if typed_username in content:
                    password = content[typed_username]
                    if password == typed_password:
                        print("Login successful.")
                    else:
                        print("Password doesn't match")
                else:
                    print("User not registered. Try signing up.")
        elif action == "3":
            if not os.path.exists(file_path):
                print("No users registered yet.")
                continue
            try:
                with open(file_path, "r") as f:
                    try:
                        content = json.load(f)
                    except Exception:
                        content = {}
            except Exception:
                content = {}
            typed_username = input("Enter your username: ").strip()
            if typed_username == "e":
                break
            if typed_username in content:
                while True:
                    password = input("Enter your new password: ")
                    if password_strength_check(password):
                        break
                content[typed_username] = password
                with open(file_path, "w") as f:
                    json.dump(content, f, indent=2, sort_keys=True)
                print("Password updated successfully.")
            else:
                print("User not registered.")
        else:
            print("Please enter correct action.")

    except FileNotFoundError:
        print("File not found, Creating new file.")
        with open(file_path, "w") as f:
            json.dump({}, f)
