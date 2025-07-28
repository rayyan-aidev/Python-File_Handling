def letter_remover():
    print("This is the letter remover.")
    while True:
        print("1-To Exit")
        original_sentence = input("Enter a sentence: ")
        sentence = []
        if original_sentence == "1":
            break
        remove_which = input(
            "Type which letters you wish to remove.(comma_seperated): ")
        if remove_which == "1":
            break
        words = original_sentence.lower().strip().split()
        to_remove = remove_which.lower().strip().replace(" ", "").split(",")
        for word in words:
            new_word = word
            for letter in to_remove:
                new_word = new_word.replace(letter, "")
            if new_word:
                sentence.append(new_word)
        print("Result:", " ".join(sentence))
    print("Letter_remover exited.")


letter_remover()
