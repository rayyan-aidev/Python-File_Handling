print("Welcome!You have entered the number guessing game. You have 5 trys to guess a number from 1 to 15. Good Luck.")
secret_number = 7
guess_limit = 5
guess = ""
guess_count = 0
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    if guess > 15 or guess < 1:
        print("Invalid guess!")
        guess_count += 1
    else:
        if guess == secret_number:
            print("You won!")
            break
        else:
            guess_count += 1
else:
    print("You lost! Try again later.")
