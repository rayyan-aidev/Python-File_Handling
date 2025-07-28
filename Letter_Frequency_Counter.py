def letter_frequency_counter():
    print("This is the Letter Frequency Counter")
    while True:
        print("1-To Exit")
        letter_count = []
        sentence = input("Enter a sentence: ")
        if sentence == "1":
            break
        sentence = sentence.strip().lower()
        letters = input(
            "Which letters would you like to count(Comma-seperated): ")
        if letters == "1":
            break
        letters = letters.lower().strip().replace(" ", "").split(",")
        for char in letters:
            letter_count.append(sentence.count(char))
        for i in range(len(letters)):
            print(
                f"\nThe letter {letters[i]} appeared {letter_count[i]} times in {sentence.title()}")
    print("You exited.")


letter_frequency_counter()
